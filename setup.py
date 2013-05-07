# -*- coding: utf8 -*-
from setuptools import setup, find_packages
import restql

setup(
    name = 'RestQL',
    version = restql.__version__,
    #packages = 'restql',
    #packages_dir = {'restql': 'restql'},
    packages = find_packages(),

    install_requires = [
        'bottle >= 0.11.6',
        'pony >= 0.4.5',
    ],

    #scripts = ['restql-run.py'],
    entry_points={
        'console_scripts': [
            'restql-run = restql.run:main',
        ],
    },

    author = 'Guillaume Luchet',
    author_email = 'guillaume@geelweb.org',
    description = 'Provides a REST API to SQL databases',
    license = 'MIT',
    keywords = 'REST SQL API Database',

    platforms = 'ALL',
)
