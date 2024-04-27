import __future__
import abc
import contextlib
import copy
import dataclasses
import logging
import math
import pathlib
import pdb
import platform
import sys
import typing
import uuid
from datetime import time
import re

import matplotlib as matplotlib
import numpy
import pandas as pandas
import psycopg2 as psycopg2
import scipy as scipy
import sqlalchemy as sqlalchemy
import toml as toml
from setuptools import setup, find_packages

setup(
    name='sttpg_qats',
    version='1.0.1',
    author='',
    author_email='',
    description='sttpg package used in QATS',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'math',
        'typing',
        'dataclasses',
        'uuid',
        'sqlalchemy',
        'psycopg2',
        'copy',
        'logging',
        'time',
        'pathlib',
        'sys',
        'platform',
        'contextlib',
        'toml',
    ],
    classifiers=[
        # Se https://pypi.org/classifiers/ for en liste over klassifikatorer
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
