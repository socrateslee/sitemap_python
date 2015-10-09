#!/usr/bin/env python

sdict = {
    'name': 'sitemap_python',
    'version': "0.1.1",
    'license': 'MIT',
    'packages': ['sitemap'],
    'zip_safe': False,
    'install_requires': [],
    'author': 'Lichun',
    'url': 'https://github.com/socrateslee/sitemap_python',
    'classifiers': [
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python']
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
