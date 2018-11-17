#!/usr/bin/env python
# encoding: utf-8

"""Packaging script."""


from setuptools import setup
setup(name='cnames',
      python_requires='>2.6',
      version='0.1',
      description='returns a tuple of the column names in the given pandas DataFrame',
      url='https://github.com/ebenp/cnames',
      author='Eben Pendleton',
      author_email='ebenp@users.noreply.github.com',
      license='MIT',
      packages=['cnames'],
      install_requires=['pandas>=0.18.1'])