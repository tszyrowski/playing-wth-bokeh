"""
Installing module

Created on 23 Aug 2019.
"""
import os 
import re
import setuptools


HERE = os.path.abspath(os.path.dirname(__file__))

VERSION_PY = ["src", "playing_with_bokeh", "version.py"]


def read(*args):
    """Read complete file contents."""
    with open(os.path.join(HERE, *args)) as fh:
        return fh.read()


def get_requirements():
    """Read the requirements file."""
    requirements = read("requirements.txt")
    return [r for r in requirements.strip().splitlines()]


def get_version():
    """Parse version from the file"""
    version_file = read(*VERSION_PY)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file,
                              re.M,
                              )
    if version_match:
        return version_match.group(1)
    
    raise RuntimeError("Unable to find version string")


setuptools.setup(
    install_requires=get_requirements(),
    version=get_version()
)
