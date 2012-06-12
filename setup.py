# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


# shamlessly stolen from Hexagon IT guys
def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('src', 'eestec', 'portal', 'version.txt').strip()

setup(name='eestec.portal',
      version=version,
      description="Enter description of what this project is all about.",
      long_description=read('README.rst') +
                       read('docs', 'HISTORY.rst') +
                       read('docs', 'LICENSE.rst'),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Python',
      author='EESTEC International',
      author_email='it@eestec.com',
      url='http://eestec.net',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['eestec'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # list project dependencies
          'niteoweb.loginas',
          'plone.app.caching',
          'plone.app.theming',
          'setuptools',
          'z3c.jbot',
      ],
      extras_require={
          # list libs needed for unittesting this project
          'test': [
              'mock',
              'plone.app.testing',
              'unittest2',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )