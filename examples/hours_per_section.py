from collections import defaultdict

import tator

def parse_args():
    parser = tator.get_parser()
    parser.add_argument('--organization', help="Organization ID.", type=int)
    args = parser.parse_args()
    return args   

def get_media(projects):
    medias = defaultdict(lambda: defaultdict(list))
    s3_keys = defaultdict(list)
    for project in projects:
        print(f"-----------------------------------------------------------")
        print(f"Retrieving data for project {project.id} ({project.name})...")
        sections = api.get_section_list(project.id)
        for section in sections:
            print(f"Retrieving data for section {section.id} ({section.name})...")
            medias[project.id][section.id] = api.get_media_list(project.id,
                                                                section=section.id,
                                                                dtype='video')
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

def sum_hours(projects, medias, clone_ids):
    hours = {}
    for project in projects:
        sections = api.get_section_list(project.id)
        print(f"-----------------------------------------------------------")
        print(f"Project {project.id} ({project.name})")
        for section in sections:
            seconds = 0.0
            for media in medias[project.id][section.id]:
                if media.id not in clone_ids:
                    if (media.num_frames is not None) and (media.fps is not None):
                        if media.fps > 0:
                            seconds += media.num_frames / media.fps
                        else:
                            print(f"WARNING: Media {media.id} has fps=0")
                    else:
                        print(f"WARNING: Media {media.id} has num_frames=None or fps=None!")
            print(f"- Section {section.id} ({section.name}): {seconds/3600.0:0.2f} hours")

if __name__ == '__main__':
    args = parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    projects = api.get_project_list(organization=args.organization)
    medias, s3_keys = get_media(projects)
    clone_ids = find_clones(s3_keys)
    sum_hours(projects, medias, clone_ids)
