#!/usr/bin/env python3
""" Tool to export localization datasets in Tator to MS-COCO (bounding box) format on-disk 

- The extraction tool can be used to generate coco datasets from video or image sources containing bounding box information.
- The tool utilizes the same annotation id in tator for annotations within the coco dataset.
- The tool is idempotent and supports inputting existing coco datasets to augment data.
- The tool can skip downloading of data to preview extractions. (--skip-download)

"""
import argparse
import os
import json
import sys
import tator
import tqdm
import shutil

from collections import defaultdict
from pprint import pprint

DEFAULT_COCO = {"info": {}, "licenses": [], "images":[], "categories":[], "annotations":[]}

def process_section(args : argparse.Namespace, 
                    api: tator.openapi.tator_openapi.TatorApi, 
                    section : tator.models.SectionSpec, 
                    images: list, 
                    categories: list,
                    annotations: list):
  """ Process a media section to MS-COCO format """
  new_images = []
  new_categories = []
  new_annotations = []

  annotation_ids = [x['id'] for x in annotations]

  category_lookup = {x['name']: x['id'] for x in categories}
  image_lookup = {x['id']: x for x in images}
  
  localization_count = api.get_localization_count(section.project, type=args.localization_type_id, section=section.id)
  localizations = []
  print(f"Fetching {localization_count} boxes")
  page_size = 5000
  localizations = api.get_localization_list(section.project, section=section.id, type=args.localization_type_id, stop=page_size)
  for _ in tqdm.tqdm(range(page_size,localization_count, page_size), desc='Batches'):
    localizations.extend(api.get_localization_list(section.project, section=section.id, type=args.localization_type_id, after=localizations[-1].id, stop=page_size))
  assert len(localizations) == localization_count
  media_objs = api.get_media_list_by_id(section.project, media_id_query={'ids': [x.media for x in localizations]})
  media_type_objs = api.get_media_type_list(section.project)
  media_type_lookup = {x.id: x for x in media_type_objs}
  media_lookup = {x.id: x for x in media_objs}
  print(f"Processing {len(localizations)} across {len(media_objs)} Media.")

  # Helper lambdas to help with loop iteration
  def find_category_id(category_name: str):
    """ Lambda to find and insert if required, insert a new category. """
    category_id = category_lookup.get(category_name, None)
    if category_id is None:
      print(f"Notice: Couldn't get category id for {category_name} given {category_lookup}")
      if category_lookup.values():
        existing_ids = [x for x in category_lookup.values()]
        new_category_id = max(existing_ids) + 1
      else:
        new_category_id = 1
      category_lookup[category_name] = new_category_id
      category_id = new_category_id
      new_categories.append({'id': new_category_id, 
                             'name':category_name, 
                             'supercategory': args.default_super_category})
    # finally return the category_id
    return category_id
          

  def handle_media_if_not_present(localization: tator.models.Localization, image_id : int):
    """ Lambda to download and add images """
    image_info = image_lookup.get(image_id, None)
    height, width, name, date_captured, media_type = get_image_info(localization)
    if args.include_image_dir:
      filename = os.path.join(args.image_dir, f"{name}_{image_id}.png")
    else:
      filename = f"{name}_{image_id}.png"
    if image_info is None:
      image_info = {'id': image_id,
                  'height': height,
                  'width': width,
                  'name': name,
                  'date_captured': date_captured,
                  'file_name': filename
                 }
      image_lookup[image_id] = image_info
      new_images.append(image_info)

    # Handle images regardless of whether it is present in case dataset needs to be
    # recreated locally
    if not args.skip_download and os.path.exists(filename) == False:
      if media_type == 'video':
        media_object = media_lookup[localization.media]
        print(f"\n\rDownloading {media_object.name} frame={localization.frame}")
        temp_path = api.get_frame(localization.media, frames=[localization.frame])
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        shutil.move(temp_path, filename)
      elif media_type == 'image':
        # Download the none AVIF source file as local tools likely don't support that
        media_object = media_lookup[localization.media]
        image_types = [x.mime for x in media_object.media_files.image]
        images_types = [x for x in image_types if x != 'image/avif']
        print(f"\n\rDownloading {media_object.name}")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        for _ in tator.util.download_media(api, media_object, filename, None, 'image', images_types[0]):
          pass

  def get_image_id(localization: tator.models.Localization):
    """ Return image information based on a localization's source media """
    media = media_lookup[localization.media]
    media_type = media_type_lookup[media.meta]
    if media_type.dtype == 'image':
      image_id = media.id
    elif media_type.dtype == 'video':
      # Generate a unique id for a given frame capture of a video
      # This is unlikely to collide with a regular image id given the shift of 64 bits
      # A collision could occur with 18,446,744,073,709,551,615 media records 
      # (roughly 18.5 quintillion records)
      image_id = (media.id << 64) | localization.frame
    else:
      print(f"{localization.id} In {media.id} which has unsupported dtype {media_type.dtype}")
      sys.exit(-1)
    return image_id

  def get_image_info(localization: tator.models.Localization):
    """ Return image information based on a localization's source media """
    media = media_lookup[localization.media]
    media_type = media_type_lookup[media.meta]
    if media_type.dtype == 'image':
      name = media.name
      date_captured =str(media.modified_datetime)
      height = media.height
      width = media.width
    elif media_type.dtype == 'video':
      name = f"{media.name}_frame{localization.frame}"
      date_captured =str(media.modified_datetime)
      if media.media_files.streaming:
        heights = [x.resolution[0] for x in media.media_files.streaming]
        widths = [x.resolution[1] for x in media.media_files.streaming]
        height = max(heights)
        width = max(widths)
      else:
        height = media.height
        width = media.width
    else:
      print(f"{localization.id} In {media.id} which has unsupported dtype {media_type.dtype}")
      sys.exit(-1)
    return height, width, name, date_captured, media_type.dtype


  def localization_to_bbox(localization: tator.models.Localization, image_id : int):
    """ Given a localization and its COCO image_id generate the bbox in COCO terms

        NOTE: COCO uses whole absolute pixels """

    image_info = image_lookup[image_id]
    x_coord = round(localization.x * image_info['width'])
    y_coord = round(localization.y * image_info['height'])
    width = round(localization.width * image_info['width'])
    height = round(localization.height * image_info['height'])
    return [x_coord,y_coord,width,height]


  for localization in tqdm.tqdm(localizations, desc="Localizations"):
    # Always handle media in case we are downloading
    image_id = get_image_id(localization)
    handle_media_if_not_present(localization, image_id)

    # Only add as a new localization if it isn't present
    if localization.id in annotation_ids:
      continue
    coco_annotation = {'iscrowd': 0, # required top-level for most training libraries
                      'id': localization.id, # use the tator-id for consistency
                      'category_id': find_category_id(localization.attributes.get(args.class_name)),
                      'image_id': image_id,
                      'bbox': localization_to_bbox(localization, image_id)
                      }
    new_annotations.append(coco_annotation)

    
    


  return new_images, new_categories, new_annotations

def main():
  """ Entry point function """
  parser = tator.get_parser(description="Export tator data to MS-COCO format")
  parser.add_argument("--skip-download",
                      action="store_true",
                      help="Skip downloading of files, useful for debugging generation")
  parser.add_argument("--localization-type-id",
                      type=int,
                      required=True,
                      help="The localization type to extract for annotation data")
  parser.add_argument("--input_coco", type=str, help='Path to COCO dataset which is used as a starting point prior to extraction')
  parser.add_argument("--image-dir", type=str, default='images', help='Path to download images to')
  parser.add_argument("--default-super-category", type=str, default='vessel', help='If a category is assumed, use this super category')
  parser.add_argument("--class-name", type=str, help='Attribute to use for classification')
  parser.add_argument("--indent", type=int, default=2, help='Indent to use on JSON file')
  parser.add_argument("--include-image-dir", action='store_true', help='Include "image-dir" path in COCO file_name property of image, else it is excluded.')
  parser.add_argument("output_file", type=str, help='Output filepath for generated JSON file')
  parser.add_argument("section",
                      type=str,
                      nargs="+",
                      help="A list of one or more media sections to process for localization data")
  args = parser.parse_args()

  dataset = {**DEFAULT_COCO}
  if args.input_coco:
    with open(args.input_coco) as file_pointer:
      dataset.update(json.load(file_pointer))

  api = tator.get_api(host=args.host, token=args.token)
  section_info = [api.get_section(section) for section in args.section]
  for section in tqdm.tqdm(section_info, desc="Section"):
    # For each section augment the existing dataset
    new_images, new_categories, new_annotations = process_section(args,
                                                                  api,
                                                                  section,
                                                                  dataset['images'],
                                                                  dataset['categories'],
                                                                  dataset['annotations'])
    dataset['images'].extend(new_images)
    dataset['categories'].extend(new_categories)
    dataset['annotations'].extend(new_annotations)

  print("\nDataset Summary:")
  print("="*80)
  print("Info:")
  pprint(dataset['info'], indent=2)
  print("License:")
  pprint(dataset['licenses'], indent=2)
  print("Populations:")
  print(f"\tImages:\t{len(dataset['images'])}")
  print(f"\tCategories:\t{len(dataset['categories'])}")
  print(f"\tAnnotations:\t{len(dataset['annotations'])}")

  category_lookup = {x['id']: x['name'] for x in dataset['categories']}
  category_histogram=defaultdict(lambda: 0)
  for annotation in dataset['annotations']:
    category_histogram[category_lookup[annotation['category_id']]] += 1

  print("Distribution:")
  category_histogram = {**category_histogram}
  pprint(category_histogram, indent=2)
  with open(args.output_file,'w') as output_file:
    json.dump(dataset, output_file, indent=args.indent)


if __name__ == "__main__":
  main()
