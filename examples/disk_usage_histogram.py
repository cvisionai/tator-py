import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

import tator

def parse_args():
    parser = tator.get_parser()
    parser.add_argument('--project', type=int, help="Project ID.")
    parser.add_argument('--max_age_days', type=int, help="Number of days since upload.")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    api = tator.get_api(args.host, args.token)
    oldest_datetime = datetime.datetime.now() - datetime.timedelta(days=args.max_age_days)
    medias = api.get_media_list(args.project,
                                search=f"_created_datetime:>{oldest_datetime.strftime('%Y-%m-%d')}")
    ratios = defaultdict(list)
    for media in medias:
        if media.num_frames is None:
            continue
        duration = media.num_frames / media.fps
        duration /= 3600
        if media.media_files:
            total = 0
            if media.media_files.streaming:
                for resource in media.media_files.streaming:
                    size = resource.size / 1024 / 1024 / 1024
                    ratios[resource.resolution[0]].append(size / duration)
                    total += size / duration
            if media.media_files.archival:
                for resource in media.media_files.archival:
                    size = resource.size / 1024 / 1024 / 1024
                    ratios['archival'].append(size / duration)
                    total += size / duration
            ratios['total'].append(total)
    categories = [f"{key}, mean={np.mean(ratios[key]):.2f}" for key in ratios]
    data = [list(np.clip(ratios[key], 0, 5)) for key in ratios]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(f'Disk usage for videos in last {args.max_age_days} days')
    ax.set_xlabel('GB/hour')
    ax.hist(data, 20, density=True, histtype='bar', label=categories, range=(0, 5), stacked=False)
    ax.legend(prop={'size': 10})
    plt.show()
