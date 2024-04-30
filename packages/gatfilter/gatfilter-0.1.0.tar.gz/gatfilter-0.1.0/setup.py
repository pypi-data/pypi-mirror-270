#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

def read(fname):
    with open(fname, "r") as fh:
        content = fh.read()
    return content


__version__ = find_version('gatfilter/__init__.py')

setup(
    name='gatfilter',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'numpy', 'pandas', 'nltk', 'matplotlib', 'scikit-learn','scipy'
    ],
    author='Sherry J.H Feng',
    author_email='xxh8511@autuni.ac.nz',
    description='A library for filtering augment text based on geometric properties',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url='https://github.com/SherryFeng123/gatfilter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Linguistic',

    ],
)
