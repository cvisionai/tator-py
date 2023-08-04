#!/usr/bin/env python

""" This example shows how to create a hierarchy of leaves for label autocomplete.
"""

import logging
import sys
import argparse
from textwrap import dedent

import yaml
import tator

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

def _create_children(api, tree, project, type_id, parent):
    children = tree.get('children')
    if children:
        specs = [{'project': project,
                  'type': type_id,
                  'name': child['name'],
                  'parent': parent} for child in children]
        response = api.create_leaf_list(project, create_leaf_list_request=specs)
        for child_id, child in zip(response.id, children):
            _create_children(api, child, project, type_id, child_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=dedent('''\
    Creates a label hierarchy with Leaf objects.

    This utility accepts a yaml file with the following format:

    name: GoT # The name of the hierarchy.
    children:
    - name: Targaryen
      children:
      - name: Maekar I
        children:
        - name: Maester Aemon
        - name: Aegon V
          children:
          - name: Jaehaerys II
            children:
            - name: Aerys II (Mad King)
              children:
              - name: Daenerys
              - name: Viserys
              - name: Rhaegar
                children:
                - name: Aegon
          - name: Rhaelle
    - name: Stark
      children:
      - name: Rickard
        children:
        - name: Brandon
        - name: Eddard
          children:
          - name: Robb
          - name: Sansa
          - name: Arya
          - name: Brandon
          - name: Rickon
        - name: Benjen
        - name: Lyanna

    Once leaves are created, the autocomplete service will be available at:
    https://<domain>/rest/Leaves/Suggestion/<project_name>.GoT/<project>

    To narrow scope of the autocomplete service (for example just Starks):
    https://<domain>/rest/Leaves/Suggestion/<project_name>.GoT.Stark/<project>

    To use an autocomplete service on a string attribute type, set the autocomplete field
    as follows:
    {...
     'autocomplete': {'serviceUrl': 'https://<domain>/rest/Leaves/Suggestion/<project_name>.GoT/<project>'},
     ...}

    '''), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--host', help='Host containing source project.', required=True)
    parser.add_argument('--token', help='Token for host containing source project.', required=True)
    parser.add_argument('--type_id', help="Leaf type ID.", type=int, required=True)
    parser.add_argument('--input', help="Path to YAML file defining label hierarchy.", type=str,
                        required=True)
    args = parser.parse_args()
    tator_api = tator.get_api(args.host, args.token)

    # Get the leaf type.
    leaf_type = tator_api.get_leaf_type(args.type_id)
    project = leaf_type.project

    # Read input file.
    with open(args.input, 'r') as f:
        tree = yaml.safe_load(f)

    # Create root leaf.
    root_spec = {
        'project': project,
        'type': leaf_type.id,
        'name': tree['name'],
    }
    response = tator_api.create_leaf_list(project=project, create_leaf_list_request=root_spec)

    # Create children recursively.
    _create_children(tator_api, tree, project, leaf_type.id, response.id[0])

