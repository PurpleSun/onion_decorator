#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tony <stayblank@gmail.com>
# Time: 2019/6/5 10:16
from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read()

setup(
    name="onion-decorator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PurpleSun/onion_decorator",
    version="0.0.1",
    keywords=("decorator", "singleton", "timeit", "memorized", "suppress_exceptions", "once", "synchronized", "qps",
              "final", "override", "deprecated", "timeout", "asynchronous", "countcalls",
              "accepts", "returns", "raises", "abstract"),
    description="A common and useful decorator library for python",
    license="MIT License",
    install_requires=["pylru>=1.2.0"],
    author="fanwei.zeng",
    author_email="stayblank@gmail.com",
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    platforms="any"
)
