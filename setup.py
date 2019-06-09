# -*- coding: utf-8 -*-
"""
This module contains the tool of oxford.testimonial
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = open(os.path.join("oxford", "testimonial", "version.txt")).read().strip()

long_description = (
    read(os.path.join('docs', 'README.txt'))
    + '\n' +
    'Installing\n'
    '**************\n'
    + '\n' +
    read(os.path.join('docs', 'INSTALL.txt'))
    + '\n' +
    'History\n'
    '**********************\n'
    + '\n' +
    read(os.path.join('docs', 'HISTORY.txt'))
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read(os.path.join('docs', 'CONTRIBUTORS.txt'))
    + '\n' +
    'Download\n'
    '********\n')

setup(name='oxford.testimonial',
      version=version,
      description="Storage mechanism for testomials",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Michael Davis',
      author_email='m.r.davis@me.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['oxford', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require = {
          'test': [
              'plone.app.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
