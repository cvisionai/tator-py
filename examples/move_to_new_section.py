# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
"""
This cell sets up the information necessary to update the section for all media in the source
section. It is safe to run repeatedly and will not make any changes to media stored in tator.
"""

# Hostname of tator cloud instance, do not change
host = "https://www.tatorapp.com"

# Your user token
token = "your-token-here"

# ID of project containing the source section
project_id = 123

# Source section, must already exist
source_section = "Source Section Name"

# Destination section, may already exist
dest_section = "New Section Name"

# +
"""
This cell tests the information set up in the previous cell. It is safe to run repeatedly and will
not make any changes to media stored in tator. It will raise an exception if it finds an issue with
any of the variables set up in the first cell. If no issues are found, it will print out information
about the source section and affected media.
"""

# Get tator api with credentials
common_err = "please fix the first cell and start over"
import tator

try:
    api = tator.get_api(host=host, token=token)
except:
    print(f"Could not get api at '{host}' with token '{token}', {common_err}")
    raise

# Test project access
try:
    api.get_project(project_id)
except:
    print(f"Could not access project with id {project_id}, {common_err}")
    raise

# Make sure source section exists
response = api.get_section_list(project=project_id, name=source_section)
assert len(response) == 1, f"No unique section matching the name '{source_section}', {common_err}"
source_section_id = response[0].id

# Get media count from source section
media_count = api.get_media_count(project=project_id, section=source_section_id)

print(
    f"Accessed project {project_id} successfully, source section '{source_section}' has id {source_section_id} and {media_count} media"
)

print("Running the next cell will move media to the new section!")

# +
"""
This cell will create the new section, move media from the source section to the new section, and
hide the empty source section from view. Running this WILL CHANGE MEDIA IN TATOR and it should ONLY
BE RUN ONCE after all preceeding cells have run without exception.
"""
from uuid import uuid4

# Create or find dest section
response = api.get_section_list(project=project_id, name=dest_section)
n_sections = len(response)

if n_sections > 1:
    raise ValueError(
        f"Found more than one section associated with name '{dest_section}', try another name"
    )

if n_sections == 1:
    new_user_section = response[0].tator_user_sections
    if not response[0].visible:
        api.update_section(id=new_section_id, section_update={"visible": True})
else:
    new_user_section = str(uuid4())
    section_spec = {"name": dest_section, "visible": True, "tator_user_sections": new_user_section}
    api.create_section(project=project_id, section_spec=section_spec)

# Create media bulk update spec
try:
    media_bulk_update = {
        "attributes": {"tator_user_sections": new_user_section},
    }
except NameError:
    print(
        "A variable from the previous cell is not set, please run it before trying to run this cell again"
    )
    raise

# Move media to dest section
response = api.update_media_list(
    project=project_id, section=source_section_id, media_bulk_update=media_bulk_update
)
print(response)

# Archive source section
response = api.update_section(id=source_section_id, section_update={"visible": False})
# -

"""
To determine the source section of a given media entity:

1. Get changelog for media in question
2. Find entry where the `tator_user_sections` attribute changed
3. Note the old value of it
4. Get the list of sections in the project
5. Find the section in the list of sections whose `tator_user_sections` value matches the value from
   line 3
6. Look at its name
"""
