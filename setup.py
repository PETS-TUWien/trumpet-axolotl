# -*- coding: utf-8 -*-

import sys

import trumpet_axolotl
from setuptools import find_packages, setup

deps = ['pycrypto', 'python-axolotl-curve25519', 'protobuf>=3.0.0.b2']

setup(
    name='trumpet_axolotl',
    version=trumpet_axolotl.__version__ ,
    packages= find_packages(),
    install_requires = deps,
    description="Modified version of python-axolotl - THIS LIBRARY HAS VULNERABILITIES (ON PURPOSE)! DO NOT USE THIS IN PRODUCTION!",
    platforms='any',
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Security :: Cryptography',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
