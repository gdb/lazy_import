#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as infile:
    readme = infile.read()

with open('lazy_import/VERSION') as infile:
    version = infile.read().strip()

tests_require = ['pytest', 'pytest-xdist']

setup(name='lazy_import_plus',
      version=version,
      description='A module for lazy loading of Python modules and lazy subclassing of pure Python classes (forked from lazy_import)',
      long_description=readme,
      url='https://github.com/gdb/lazy_import',
      author='Greg Brockman',
      author_email='gdb@gregbrockman.com',
      license='GPL',
      platforms = ["any"],
      classifiers=['Development Status :: 4 - Beta',
                   # Indicate who your project is intended for
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Libraries :: '
                     'Python Modules',

                   'License :: OSI Approved :: '
                     'GNU General Public License v3 or later (GPLv3+)',

                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',

                   'Operating System :: OS Independent',
                   ],
      packages=find_packages(),
      install_requires=['six'],
      test_suite='lazy_import.test_lazy',
      tests_require=tests_require,
      extras_require={'test': tests_require},
      package_data={'lazy_import': ['VERSION']}
      )
