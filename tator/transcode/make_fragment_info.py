#!/usr/bin/python3

import argparse
import json
import sys
import subprocess

FRAGMENT_VERSION=2

def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("input", help="MP4 File", type=str)
    parser.add_argument("-o", "--output")
    return parser.parse_args()

def make_fragment_info(video_file, output):
    cmd=["mp4dump",
         "--format",
         "json",
         video_file]
    proc=subprocess.Popen(cmd, stdout=subprocess.PIPE)
    mp4_data,error=proc.communicate()

    cmd=["ffprobe",
         "-v",
         "error",
         "-show_entries",
         "stream",
         "-print_format",
         "json",
         "-select_streams", "v",
         video_file]
    proc=subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ffprobe_output,error=proc.communicate()

    ffprobe_data=json.loads(ffprobe_output)
    start_time = 0
    try:
        for stream in ffprobe_data["streams"]:
            if stream["codec_type"] == "video":
                start_time=float(ffprobe_data["streams"][0]["start_time"])
                break
    except Exception as e:
        print(e)

    outputFile=sys.stdout
    if output != None:
        outputFile=open(output, "w")

    currentOffset=0
    currentFrame=0
    info={"file": {"start": start_time, "version": FRAGMENT_VERSION}, "segments" : []}
    with open(video_file) as fp:
        obj=json.loads(mp4_data)
        for data in obj:
            block={"name": data['name'],
                   "offset": currentOffset,
                   "size": data['size']}

            # Add time offset for moof blocks
            if block['name'] == 'moof':
                for child in data['children']:
                    if child['name'] == 'traf':
                        for grandchild in child['children']:
                            if grandchild['name'] == 'trun':
                                block['frame_start'] = currentFrame
                                block['frame_samples'] = grandchild['sample count']
                                currentFrame += grandchild['sample count']
            info['segments'].append(block)

            currentOffset+=block['size']


    json.dump(info, outputFile)

if __name__=="__main__":
    args = parse_args()
    make_fragment_info(args.input, args.output)
