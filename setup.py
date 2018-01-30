# -*- coding: utf-8 -*-

from setuptools import setup

try:
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name='wisdomhord',
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    description='',
    long_description=readme,
    packages=['wisdomhord'],
    install_requires=[
        'datarum>=0.2.0'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    use_scm_version=True
)
