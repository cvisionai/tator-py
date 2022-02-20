import subprocess

import tator

def test_leaf(host, token, project, leaf_type, video_type):
    cmd = [
        'python3',
        'examples/leaf.py',
        '--host', host,
        '--token', token,
        '--type_id', str(leaf_type),
        '--input', 'examples/leaf.yaml',
    ]
    subprocess.run(cmd, check=True)
    # Apply the label tree to string fields for media types
    api = tator.get_api(host, token)
    api.rename_attribute(video_type, {
        'entity_type': 'MediaType',
        'global': 'true',
        'old_attribute_type_name': 'test_string',
        'new_attribute_type': {
            'name': 'test_string',
            'dtype': 'string',
            'autocomplete': {'serviceUrl': f'/rest/Leaves/Suggestion/GoT/{project}'}
        },
    })
    
