#!/usr/bin/python3
""" 
Takes a config file like so to export a tator project to disk:

```
export:
  project: 93
  token: <TOKEN>
  host: http://local.tator.io
import:
  project: 94
  token: <TOKEN>
  host: http://local.tator.io
```
"""

import tator
import argparse
import yaml
import os
import json
import math
import tqdm

from tator.util._download_file import _download_file

def response_to_disk(response, path):
  """ Helper function to a response to disk """
  if type(response) == list:
    with open(path, 'w') as fp:
      output_object = []
      for r in response:
        output_object.append(r.to_dict())
      json.dump(output_object, fp, default=str)
  else:
    with open(path, 'w') as fp:
      json.dump(response.to_dict(), fp, default=str)

def download_project_info(config, output_dir):
  api = tator.get_api(host=config['host'], token=config['token'])
  project_id = config['project']

  # Output project info, memberships, and users
  project_info = api.get_project(project_id)
  response_to_disk(project_info, os.path.join(output_dir, "project.json"))
  
  memberships = api.get_membership_list(project_id)
  response_to_disk(memberships, os.path.join(output_dir, "memberships.json"))


  users = []
  for m in memberships:
    users.append(api.get_user(m.user))
  
  response_to_disk(users, os.path.join(output_dir, "users.json"))

  # Output all type objects
  lookup_map = {"localization": api.get_localization_type_list,
                "media" : api.get_media_type_list,
                "state" : api.get_state_type_list,
                "file" : api.get_file_type_list,
                "leaf" : api.get_leaf_type_list}

  type_count = {}
  for name, accessor in lookup_map.items():
    response = accessor(project_id)
    type_count[name] = len(response)
    response_to_disk(response, os.path.join(output_dir, f"{name}_types.json"))

  lookup_map = {"localization": (api.get_localization_list, api.get_localization_count),
                "media" : (api.get_media_list, api.get_media_count),
                "state" : (api.get_state_list,api.get_state_count),
                "file" : (api.get_file_list,None),
                "leaf" : (api.get_leaf_list, api.get_leaf_count)}

  BATCH_SIZE = 10000
  for name, (accessor, count) in lookup_map.items():
    if type_count[name] == 0:
      print(f"Notice: No registered types for '{name}'")
      response_to_disk([], os.path.join(output_dir, f"{name}s.json"))
    elif count:
      element_count = count(project_id)
      batches = math.ceil(element_count / BATCH_SIZE)
      total_set = []
      for batch_idx in range(batches):
        response = accessor(project_id, start=batch_idx*BATCH_SIZE, stop=(batch_idx+1)*BATCH_SIZE)
        total_set.append(*response)
      assert len(total_set) == element_count
      response_to_disk(total_set, os.path.join(output_dir, f"{name}s.json"))
    else:
      response = accessor(project_id)
      response_to_disk(response, os.path.join(output_dir, f"{name}s.json"))
  print("Notice: Metadata export compete.")



def download_media_files(config, project_dir):
  api = tator.get_api(host=config['host'], token=config['token'])
  project_id = config['project']
  media_dir = os.path.join(project_dir, "Medias")
  os.makedirs(media_dir, exist_ok=True)
  element_count = api.get_media_count(project_id)
  BATCH_SIZE = 100
  batches = math.ceil(element_count / BATCH_SIZE)
  print(f"Downloading {element_count} medias in {batches} sets")
  for batch_idx in tqdm.tqdm(range(batches)):
    response = api.get_media_list(project_id, presigned=24*3600,start=batch_idx*BATCH_SIZE, stop=(batch_idx+1)*BATCH_SIZE)
    for media in response:
      this_media_dir = os.path.join(media_dir, f"{media.id}")
      os.makedirs(this_media_dir, exist_ok=True)
      local_thumb = os.path.join(this_media_dir, "thumbnail.jpg")
      local_thumb_gif = os.path.join(this_media_dir, "thumbnail_gif.gif")

      if media.media_files.thumbnail and os.path.exists(local_thumb) is False:
        for _ in tator.util.download_media(api, media, local_thumb, None, "thumbnail"):
          pass

      if media.media_files.thumbnail_gif and os.path.exists(local_thumb_gif) is False:
        for _ in tator.util.download_media(api, media, local_thumb_gif, None, "thumbnail_gif"):
          pass

      archival = media.media_files.archival if media.media_files.archival else []
      for resource in archival:
        local = os.path.join(this_media_dir, "archival")
        os.makedirs(local, exist_ok=True)
        name = os.path.basename(resource.path).split('?')[0]
        download_path = os.path.join(local, name)
        for _ in _download_file(api, project_id, resource.path, download_path):
          pass
        

      streaming = media.media_files.streaming if media.media_files.streaming else []
      for resource in streaming:
        local = os.path.join(this_media_dir, "streaming")
        os.makedirs(local, exist_ok=True)
        name = os.path.basename(resource.path).split('?')[0]
        download_path = os.path.join(local, name)
        for _ in _download_file(api, project_id, resource.path, download_path):
          pass
        # Download segment info too
        name = os.path.basename(resource.segment_info).split('?')[0]
        download_path = os.path.join(local, name)
        for _ in _download_file(api, project_id, resource.segment_info, download_path):
          pass

      streaming = media.media_files.audio if media.media_files.audio else []
      for resource in streaming:
        local = os.path.join(this_media_dir, "audio")
        os.makedirs(local, exist_ok=True)
        name = os.path.basename(resource.path).split('?')[0]
        download_path = os.path.join(local, name)
        for _ in _download_file(api, project_id, resource.path, download_path):
          pass


    


def main():
  parser = argparse.ArgumentParser(description="Tool to download a tator project to an on-disk format")
  parser.add_argument("configuration", help="Path to the configuration file to use for tator configuration elements")
  parser.add_argument("output_dir", help="Directory to download project files")
  parser.add_argument("--skip-media", action="store_true", help="Skip downloading actual media resources.")
  args = parser.parse_args()
  with open(args.configuration) as fp:
    config = yaml.safe_load(fp)
    config = config['export']
  
  os.makedirs(args.output_dir, exist_ok=True)
  project_dir = os.path.join(args.output_dir, f"{config['project']}")
  os.makedirs(project_dir, exist_ok=True)
  download_project_info(config, project_dir)

  if args.skip_media:
    print("NOTICE: Skipping media download")
  else:
    download_media_files(config, project_dir)



if __name__=="__main__":
  main()