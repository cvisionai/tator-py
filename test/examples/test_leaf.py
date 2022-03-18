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
    video_type_obj = api.get_media_type(video_type)
    project_obj = api.get_project(project)
    attribute_type = {}
    for elem in video_type_obj.attribute_types:
        if elem.name == 'test_string':
            attribute_type = elem
            break
    attribute_type.autocomplete = {'serviceUrl': f'/rest/Leaves/Suggestion/{project_obj.name}.GoT/{project}'}
    api.rename_attribute(video_type, {
        'entity_type': 'MediaType',
        'global': 'true',
        'old_attribute_type_name': 'test_string',
        'new_attribute_type': attribute_type,
    })
    
