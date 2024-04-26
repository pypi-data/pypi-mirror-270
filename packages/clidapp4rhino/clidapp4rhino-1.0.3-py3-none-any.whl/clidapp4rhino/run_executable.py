import subprocess

import pkg_resources


def main():
    executable_path = pkg_resources.resource_filename(
        "clidapp4rhino", "clidapp4rhino"
    )
    subprocess.call([executable_path])
