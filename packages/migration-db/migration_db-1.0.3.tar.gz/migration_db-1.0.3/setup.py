#!/usr/bin/env python

import re
import setuptools

version = ""
with open('migration_db/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="migration_db",
    version=version,
    author="xiaodong.li",
    author_email="",
    description="Migrate database files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://example.com",
    install_requires=[
        'lxml>=4.8.0',
        'redis>=4.3.1',
        'jinja2',
    ],
    packages=setuptools.find_namespace_packages(exclude=("test")),
    classifiers=(
        "Programming Language :: Python :: 3.9",
    )
)