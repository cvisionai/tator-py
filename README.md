# tator

Python client for [Tator](https://github.com/cvisionai/tator).

## Requirements

Python 2.7 and 3.4+

## Installation

### From pypi
```
pip install tator
```

### From source
```
python setup.py install --user
```

## Example usage
```
import tator

api = tator.get_api('https://www.tatorapp.com', 'MY_TOKEN')
api.get_media_list(1) # Pass a project ID
```

Visit the [examples](examples) for more.

## API documentation

Documentation for all API functions and models can be found in the [OpenAPI documentation](tator/openapi/docs).

## Authors

Tator and tator-py are developed by [CVision AI](www.cvisionai.com).

