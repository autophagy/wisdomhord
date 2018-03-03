# -*- coding: utf-8 -*-

from setuptools import setup
from wisdomhord import __version__

setup(
    name='wisdomhord',
    version=__version__,
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    description='Flat file db tool',
    long_description="""
Wísdómhord is a flat file database tool for internal project use.

The main goal of Wísdómhord is to create a flat file db format that produces
files that are in line with my aesthetics, are easy to read and make sense to
check into Github.

.. image:: http://scieldas.autophagy.io/rtd/wisdomhord.png
    :target: http://wisdomhord.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: http://scieldas.autophagy.io/travis/Autophagy/wisdomhord.png
    :target: https://travis-ci.org/Autophagy/wisdomhord
    :alt: Build Status

.. image:: http://scieldas.autophagy.io/licenses/MIT.png
   :target: LICENSE
   :alt: MIT License""",
    packages=['wisdomhord'],
    install_requires=[
        'datarum==0.5.0'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
