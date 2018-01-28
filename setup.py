#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from wisdomhord import __version__

setup(
    name='wisdomhord',
    version=__version__,
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    url='https://github.com/Autophagy/wisdomhord',
    description='',
    long_description=open('README.rst', encoding='utf-8').read(),
    packages=['wisdomhord'],
    install_requires=[
        'datarum==0.2.0'
    ],
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
