# setup.py
import pathlib
from setuptools import setup, find_packages
import pkg_resources
import os

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

def read_version(fname="faster_whisper_api_proxy/version.py"):
    exec(compile(open(fname, encoding="utf-8").read(), fname, "exec"))
    return locals()["__version__"]


setup(
    name='faster_whisper_api_proxy',  # Name of your module
    description='a python module that is a drop in replacement for faster_whisper but calls a remote faster_whisper implementation via API',
    long_description=README,
    long_description_content_type="text/markdown",
    version=read_version(),
    url='https://github.com/rkilchmn/faster_whisper_api_proxy',
    author='Roger Kilchenmann',
    author_email='roger@kilchenmann.net',
    keywords=['AI','faster_whisper','transcribe','natural language','speech recognition','api','remote'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)
