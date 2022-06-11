#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='ru-relation-extraction',
    version='0.0.0',
    description='Narrative analysis in Python',
    long_description=readme + '\n\n' + doclink + '\n\n',
    author='',
    author_email='',
    url='',
    packages=[
        *find_packages()
        #'narcy',
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pylint',
        'pytest-pylint',
        'pytest-profiling',
        'pytest-benchmark',
        'coverage'
    ],
    test_suite='tests',
    package_dir={'narcy': 'narcy'},
    include_package_data=True,
    install_requires=[
        'spacy>=2.0.18',
        'pandas>=0.23.4',
        'nltk>=3.4'
    ],
    license='None',
    zip_safe=False,
    keywords='ru-relation',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
