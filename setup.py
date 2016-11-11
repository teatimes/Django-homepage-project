#!/usr/bin/env python
from setuptools import setup

setup(
	name='Django-homepage',
  version='1.0',
  description='OpenShift App',
  author='Dora Oline Eriksrud',
  url='http://www.python.org/sigs/distutils-sig/',
  install_requires=[
  	'Django>=1.8,<1.9',
  	'django-pagedown',
  	'django-markdown-deux',

  	],
)
