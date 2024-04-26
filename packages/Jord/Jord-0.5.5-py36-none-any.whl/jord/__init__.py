#!/usr/bin/env python3


from pathlib import Path

from apppath import AppPath

try:
    from importlib.resources import files
    from importlib.metadata import PackageNotFoundError
except (ModuleNotFoundError, ImportError) as e:
    from importlib_metadata import PackageNotFoundError
    from importlib_resources import files

from warg import package_is_editable, clean_string, get_version

__project__ = "Jord"
__author__ = "Christian Heider Lindbjerg"
__version__ = "0.5.5"
__doc__ = r"""
.. module:: jord
   :platform: Unix, Windows
   :synopsis: A set of general tools build for geo data.

.. moduleauthor:: Christian Heider Lindbjerg <chen@mapspeople.dk>

Created on 27/04/2019

@author: cnheider
"""

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()

PROJECT_NAME = clean_string(__project__)
PROJECT_VERSION = __version__
PROJECT_YEAR = 2018
PROJECT_AUTHOR = clean_string(__author__)
PROJECT_ORGANISATION = clean_string("Automaps")
PROJECT_APP_PATH = AppPath(app_name=PROJECT_NAME, app_author=PROJECT_AUTHOR)
INCLUDE_PROJECT_READMES = False
VERBOSE = False

PACKAGE_DATA_PATH = files(PROJECT_NAME) / "data"

try:
    DEVELOP = package_is_editable(PROJECT_NAME)
except PackageNotFoundError as e:
    DEVELOP = True

__version__ = get_version(__version__, append_time=DEVELOP)

__version_info__ = tuple(int(segment) for segment in __version__.split("."))

if __name__ == "__main__":
    print(PROJECT_APP_PATH.user_cache)
