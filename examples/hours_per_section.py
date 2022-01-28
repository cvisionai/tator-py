from collections import defaultdict
import os

import tator

def parse_args():
    parser = tator.get_parser()
    parser.add_argument('--organization', help="Organization ID.", type=int)
    parser.add_argument('--archive_lifecycle', help="Archive lifecycle of queried media.",
                        choices=['live', 'archived', 'all'], type=str)
    parser.add_argument('--out_dir', help="Where summary CSV files will be dumped.", type=str)
    args = parser.parse_args()
    return args   

def get_media(args, projects):
    medias = defaultdict(lambda: defaultdict(list))
    s3_keys = defaultdict(list)
    for project in projects:
        print(f"-----------------------------------------------------------")
        print(f"Retrieving data for project {project.id} ({project.name})...")
        sections = api.get_section_list(project.id)
        for section in sections:
            print(f"Retrieving data for section {section.id} ({section.name})...")
            media_kwargs = {'section': section.id,
                            'dtype': 'video'}
            if args.archive_lifecycle:
                media_kwargs['archive_lifecycle'] = args.archive_lifecycle
            medias[project.id][section.id] = api.get_media_list(project.id, **media_kwargs)
            for media in medias[project.id][section.id]:
                if media.media_files:
                    if media.media_files.streaming:
                        for media_file in media.media_files.streaming:
                            s3_keys[media_file.path].append((media, section, project))
    return (medias, s3_keys)

def find_clones(s3_keys): 
    clone_ids = set()
    for s3_key in s3_keys:
        if len(s3_keys[s3_key]) > 1:
            # Attack of the clones!
            medias, sections, projects = zip(*s3_keys[s3_key])
            lowest_idx = 0
            lowest_id = medias[0].id
            # Find the index with lowest media ID (presumed original).
            for idx, media in enumerate(medias):
                if media.id < lowest_id:
                    lowest_idx = idx
                    lowest_id = media.id
            # List out media that was a clone.
            print(f"-----------------------------------------------------------")
            print(f"The following are clones of media {lowest_id} and will be excluded.")
            for idx, media in enumerate(medias):
                if media.id != lowest_id:
                    section = sections[idx].name
                    project = projects[idx].name
                    print(f"    - Media {media.id}, section {section}, project {project}")
                    clone_ids.add(media.id)
    return clone_ids

def sum_hours(projects, medias, clone_ids, out_dir):
    hours = {}
    project_totals = defaultdict(float)
    for project in projects:
        log = open(os.path.join(out_dir, f'project_{project.id}_{project.name}.log'), 'w')
        csv = open(os.path.join(out_dir, f'project_{project.id}_{project.name}.csv'), 'w')
        sections = api.get_section_list(project.id)
        print(f"-----------------------------------------------------------")
        csv.write(f"section_id,section_name,num_files,hours\n")
        print(f"Project {project.id} ({project.name})")
        log.write(f"Project {project.id} ({project.name})\n")
        project_totals[project.id] = 0
        for section in sections:
            seconds = 0.0
            for media in medias[project.id][section.id]:
                if media.id not in clone_ids:
                    if (media.num_frames is not None) and (media.fps is not None):
                        if media.fps > 0:
                            seconds += media.num_frames / media.fps
                        else:
                            print(f"WARNING: Media {media.id} has fps=0")
                            log.write(f"WARNING: Media {media.id} has fps=0\n")
                    else:
                        print(f"WARNING: Media {media.id} has num_frames=None or fps=None!")
                        log.write(f"WARNING: Media {media.id} has num_frames=None or fps=None!\n")
            project_totals[project.id] += seconds
            print(f"- Section {section.id} ({section.name}): {seconds/3600.0:0.2f} hours")
            log.write(f"- Section {section.id} ({section.name}): {seconds/3600.0:0.2f} hours\n")
            csv.write(f"{section.id},{section.name},{len(medias)},{seconds/3600.0:0.2f}\n")
        log.close()
        csv.close()
    total_csv = open(os.path.join(out_dir, 'project_totals.csv'), 'w')
    total_csv.write('project_id,project_name,hours\n')
    for project in projects:
        total_csv.write(f'{project.id},{project.name},{project_totals[project.id]/3600.0:0.2f}\n')

if __name__ == '__main__':
    args = parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    projects = api.get_project_list(organization=args.organization)
    medias, s3_keys = get_media(args, projects)
    clone_ids = find_clones(s3_keys)
    sum_hours(projects, medias, clone_ids, args.out_dir)
