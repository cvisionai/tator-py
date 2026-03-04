#!/usr/bin/python3

import json
import os

_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
if os.path.exists(_config_path):
    with open(_config_path, 'r') as f:
        __version__ = json.load(f).get('packageVersion', '0.0.0.dev0')
else:
    __version__ = '0.0.0.dev0'

if __name__ == '__main__':
    print(__version__)
