import tator

if __name__ == '__main__':
    parser = tator.get_parser()
    args = parser.parse_args()
    api = tator.get_api(host=args.host, token=args.token)
    projects = api.get_project_list()
    total_size = 0
    total_duration = 0
    for project in projects:
        stats = api.get_media_stats(project.id)
        total_size += stats.total_size
        total_duration += stats.duration
    print(f"Total size: {total_size} bytes")
    print(f"Total duration: {total_duration} seconds")
