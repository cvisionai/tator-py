from collections import defaultdict

import tator

if __name__ == '__main__':
    parser = tator.get_parser()
    args = parser.parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    projects = api.get_project_list()
    total_size = 0
    total_duration = 0
    size_by_org = defaultdict(int)
    duration_by_org = defaultdict(int)
    for project in projects:
        stats = api.get_media_stats(project.id)
        print(f"Project {project.id} ({project.name}): {stats.total_size / 1e12:0.2f}TB, {stats.duration / 3600:0.2f} hours")
        size_by_org[project.organization] += stats.total_size
        duration_by_org[project.organization] += stats.duration
        total_size += stats.total_size
        total_duration += stats.duration
    print(f"-----------------------------------------------------------")
    for org in size_by_org.keys():
        print(f"Organization {org}: {size_by_org[org] / 1e12:0.2f}TB, {duration_by_org[org] / 3600:0.2f} hours")
    print(f"-----------------------------------------------------------")
    print(f"Total size: {total_size / 1e12:0.2f} TB")
    print(f"Total duration: {total_duration / 3600:0.2f} hours")
