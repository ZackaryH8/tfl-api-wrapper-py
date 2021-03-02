import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.0'
PACKAGE_NAME = 'tfl-api-wrapper'
AUTHOR = 'zackaryh8'
AUTHOR_EMAIL = 'zackary12389@yahoo.co.uk'
URL = 'https://github.com/you/your_package'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Describe your package in one sentence'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = []

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
