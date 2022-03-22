#!/usr/bin/env python3

""" Uses ENV variables to dispatch the frame extractor 

Generic TATOR workflow env variables this module expects:

TATOR_API_SERVICE : URL to host, e.g. https://cloud.tator.io
TATOR_AUTH_TOKEN : Token to use for authentication
TATOR_PROJECT_ID : numerical id of the project this algorithm is being run
TATOR_MEDIA_IDS : Comma-seperated list of media ids to process

:Workflow variables:
`python3 -m tator.extractor --help` for more information on the following
options:
EXTRACT_MODE : Maps to the `--mode` argument
METADATA_TYPE_ID : Maps to the `--metadata-type-id` argument
OUTPUT_SECTION : Maps to the `--tator-output-section` argument
OUTPUT_TYPE_ID : Maps to the `--output-type-id` argument  

"""
    
import os
import pandas as pd
import subprocess
import json
import sys
import shutil

if __name__=="__main__":
    media_ids = os.getenv('TATOR_MEDIA_IDS').split(',')
    cmd = ["python3",
           "-m", "tator.extractor",
           '--host', os.getenv("TATOR_API_SERVICE").replace('/rest',''),
           "--token",
           os.getenv("TATOR_AUTH_TOKEN"),
           "--mode", os.getenv("EXTRACT_MODE"),
           "--metadata-type-id", os.getenv("METADATA_TYPE_ID"),
           "--project", os.getenv("TATOR_PROJECT_ID"),
           "--output-tator-section", os.getenv("OUTPUT_SECTION"),
           "--output-type-id", os.getenv("OUTPUT_TYPE_ID"),
           # Assume PVC is located at work
           "--work-dir", "/work",
           *media_ids]

    p=subprocess.Popen(cmd)
    p.wait()
    sys.exit(p.returncode)
    
