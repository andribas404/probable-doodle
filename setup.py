# -*- coding: utf-8 -*-

from distutils.core import setup
from pathlib import Path


def get_readme():
    return open(Path(__file__).parent / "README.md").read()


setup(
    name="probable-doodle",
    packages=["probable_doodle"],
    version="0.1.0",
    description="Probable doodle.",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="Andrey Petukhov",
    author_email="andribas404@gmail.com",
    url="https://github.com/andribas404/probable-doodle",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
