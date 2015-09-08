#!/usr/bin/env python

import subprocess
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup, Command

try:
   import pypandoc
   readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
   readme = ''

setup(name='todo_list',
      version='0.0.1',
      description='Todo_list may quite possibly be the most simplistic remotely available todo list ever created.',
      long_description=readme,
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/todo_list',
      license="MIT",
      py_modules=['todo_list'],
      entry_points={
        'console_scripts': [
            'todo_list = todo_list:todo.cli',
        ]
      },
      requires=['hug', 'hot_redis', 'requests'],
      install_requires=['hug', 'hot_redis', 'requests'],
      keywords='Todo, Python, Python3',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Utilities'])