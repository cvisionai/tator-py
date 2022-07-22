import json
import os
import re
import subprocess
import shutil

import requests
import toml
import yaml


SCHEMA_FILENAME = "schema.yaml"
CONFIG_FILENAME = "config.json"
PYPROJECT_TOML = "pyproject.toml"


def remove_oneof(data):
    """Removes oneOf key from a dict and recursively calls this function on
    other dict values.
    """
    if "oneOf" in data:
        del data["oneOf"]
    for key in data:
        if isinstance(data[key], dict):
            remove_oneof(data[key])
    return data


class NoAliasDumper(yaml.Dumper):
    def ignore_aliases(self, data):
        return True


def codegen():
    """Fetches a schema from cloud.tator.io if one does not exist, then
    use openapi-generator to generate openapi code from it.
    """
    # Retrieve schema if it does not exist.
    if not os.path.exists(SCHEMA_FILENAME):
        response = requests.get("https://cloud.tator.io/schema")
        assert response.status_code == 200
        with open(SCHEMA_FILENAME, "wb") as f:
            f.write(response.content)

    # Remove any oneOf entries from the schema, as they are not handled
    # well by openapi generator.
    with open(SCHEMA_FILENAME, "r") as f:
        schema = yaml.safe_load(f)
    schema = remove_oneof(schema)
    with open(SCHEMA_FILENAME, "w") as f:
        yaml.dump(schema, f, Dumper=NoAliasDumper)

    # Get the git SHA ID.
    cmd = ["git", "rev-parse", "HEAD"]
    git_rev = subprocess.check_output(cmd).strip().decode("utf-8")

    # Generate the config file containing the version info for openapi
    pyproject = toml.load(PYPROJECT_TOML)
    version = pyproject["tool"]["poetry"]["version"]
    config_json = {
        "packageName": "tator_openapi",
        "projectName": "tator_openapi",
        "packageVersion": version,
    }
    with open(CONFIG_FILENAME, "w") as fp:
        json.dump(config_json, fp, sort_keys=True, indent=4)

    # Generate code using openapi generator docker image.
    pwd = os.path.dirname(os.path.abspath(__file__))
    cmd = [
        "docker",
        "run",
        "-it",
        "--rm",
        "-v",
        f"{pwd}:/pwd",
        "-v",
        f"{pwd}/out:/out",
        "openapitools/openapi-generator-cli:v4.3.1",
        "generate",
        "-c",
        f"/pwd/{CONFIG_FILENAME}",
        "-i",
        f"/pwd/{SCHEMA_FILENAME}",
        "-g",
        "python",
        "-o",
        f"/out/tator-py-{git_rev}",
        "-t",
        "/pwd/templates",
    ]
    subprocess.run(cmd, check=True)

    # Remove the schema and config
    os.remove(SCHEMA_FILENAME)
    os.remove(CONFIG_FILENAME)

    # Copy relevant directories into openapi.
    out_dir = os.path.join(pwd, "tator/openapi")
    os.makedirs(out_dir, exist_ok=True)
    for subpath in ["README.md", "tator_openapi", "docs"]:
        src = f"{pwd}/out/tator-py-{git_rev}/{subpath}"
        dst = os.path.join(out_dir, f"{subpath}")
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    pwd = os.path.dirname(os.path.abspath(__file__))

    # need to delete from within docker
    cmd = [
        "docker",
        "run",
        "-it",
        "--rm",
        "-v",
        f"{pwd}/out:/out",
        "openapitools/openapi-generator-cli:v4.3.1",
        "rm",
        "-fr",
        "/out/*",
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    codegen()
