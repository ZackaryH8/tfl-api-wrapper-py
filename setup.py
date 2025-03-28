import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

setup(
    name="tflwrapper",
    version="1.1.9",
    description="A wrapper for the Transport for London Unified API and TrackerNet",
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="zackaryh8",
    license="MIT",
    author_email="zackary12389@yahoo.co.uk",
    url="https://github.com/ZackaryH8/tfl-api-wrapper-py",
    install_requires=[
        "xmltodict"
    ],
    packages=find_packages(),
)
