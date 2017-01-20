#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyrtf-ng - The next generation in Rich Text Format documents for Python.

pyrtf-ng is a pure python module for the efficient creation and parsing of rich
text format documents. Supports styles, tables, cell merging, jpg and png
images and tries to maintain compatibility with as many RTF readers as
possible. 
"""

from setuptools import setup

requirements = [
    'pyparsing'
]

test_requirements = [
    'nose'
]

doclines = __doc__.split("\n")

packageName = 'rtfng'

setup(name = packageName,
    version = open('VERSION').read().strip(),
    author = 'Duncan McGreggor',
    author_email = 'oubiwann@adytum.us',
    url = 'https://github.com/shvechikov/python-rtfng',
    license = 'MIT',
    platforms = ['Any'],
    description = doclines[0],
    long_description = '\n'.join( doclines[2:]),
    keywords = ('RTF', 'Rich Text', 'Rich Text Format', 'documents', 'word'),
    packages = [packageName],
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=True,
    include_package_data=True,
    classifiers = [f.strip() for f in """
        Development Status :: 4 - Beta
        Topic :: Text Editors :: Text Processing
        Topic :: Software Development :: Libraries :: Python Modules
        Intended Audience :: Developers
        Programming Language :: Python
        License :: OSI Approved :: MIT
    """]
)
