#!/usr/bin/env python

"""
This is a setup script file for MetaRon -- a Metagenomic opeRon prediction pipeline.
This is a freeware; user is allowed to redistribute it and/or modify it under the terms and
conditions of BSD License (see the file LICENSE.mc included with the distribution).
@version: 1.0
@author: Syed Shujaat Ali Zaidi
@email: syedshujaat@comsats.edu.pk; syedzaidi85@hotmail.co.uk
"""


import pathlib
import os
from distutils.core import setup
from setuptools import find_packages
## from setuptools import setup

#from metaron import __version__

VERSION = __import__("metaron").__version__

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
]

install_requires = [
    'argparse'
	
]

setup(
    name="metaron",
    description="Metagenomic opeRon prediction pipeline",
    version=VERSION,
    author="Syed Shujaat Ali Zaidi",
    #Keywords= "bioinformatics,metagenomics, operon prediction",
    author_email="syedshujaat@comsats.edu.pk, syedzaidi85@hotmail.co.uk",
    url="https://github.com/zaidissa/MetaRon",
    package_dir={'metaron': 'metaron'},
    packages=['metaron'],
    scripts=['metaron/metaron',
                   ],
    
    install_requires = install_requires,
    classifiers=CLASSIFIERS,
)