#!/usr/bin/env python
import os
del os.link

long_description = ""

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    pass

sdict = {
    'name': 'sitemap_python',
    'version': "0.2.0",
    'license': 'MIT',
    'packages': ['sitemap'],
    'zip_safe': False,
    'install_requires': ['six'],
    'author': 'Lichun',
    'long_description': long_description,
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
