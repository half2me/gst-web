#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='gst-web',
      version='1.0',
      description='A Web UI for Building, Debugging and Controlling Gstreamer Pipelines',
      url='https://github.com/half2me/gst-web',
      author='Benjamin Tamasi',
      author_email='h@lfto.me',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3.6',
      install_requires=[
          'aiohttp',
          'aiofiles',
          'gbulb',
      ],
      zip_safe=False)
