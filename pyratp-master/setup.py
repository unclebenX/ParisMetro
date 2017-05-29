# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# TODO add dependencies {urllib3}
setup(name='pyratp',
      version='1.0.0.dev1',
      description='Python wrapper to RATP open data API',
      long_description="This Python package eases the access to the RATP (Paris' subway operator) open data platform",
      url='https://github.com/paronax/pyratp',
      author='paronax',
      license='GNU GPLv2',
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Programming Language :: Python :: 3'],
      keywords='API RATP OpenData',
      install_requires=['urllib3'],
      packages=find_packages(),
      test_suite='pyratp.tests'
)
