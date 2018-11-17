#!/usr/bin/env python
# encoding: utf-8

"""Packaging script."""


from setuptools import setup
setup(name='cnames',
      version='0.1',
      description='returns a tuple of the column names in the given pandas DataFrame',
      url='https://github.com/ebenp/cnames',
      author='Eben Pendleton',
      author_email='',
      license='MIT',
      packages=['cnames'],
      install_requires=['pandas>=0.18.1',
                        'python>=2.6'])