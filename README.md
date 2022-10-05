# tator

Python client for [Tator](https://github.com/cvisionai/tator).

## Requirements

Python 3.6+

## Installation

### From pypi
```
pip install tator
```

### From source
```
pip3 install -r requirements.txt --user
python3 setup.py install --user
```

## Example usage
```
import tator

api = tator.get_api('https://cloud.tator.io', 'MY_TOKEN')
api.get_media_list(1) # Pass a project ID
```

Visit the [examples](examples) for more.

## API documentation

Documentation for all API functions and models can be found in the [OpenAPI documentation](https://tator.io/api).

## Authors

Tator and tator-py are developed by [CVision AI](https://www.cvisionai.com).

