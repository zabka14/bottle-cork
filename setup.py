#!/usr/bin/env python

from setuptools import setup
from cork import __version__

CLASSIFIERS = map(str.strip,
"""
Environment :: Console
License :: OSI Approved :: GNU Lesser General Public License (LGPL)
Natural Language :: English
Operating System :: POSIX :: Linux
Programming Language :: Python
Topic :: Internet :: WWW/HTTP :: WSGI
""".splitlines())

setup(
    name="bottle-cork",
    version = __version__,
    author = "Federico Ceratto",
    author_email = "federico.ceratto@gmail.com",
    description = "Authentication/Authorization library for Bottle",
    license = "LGPLv3+",
    url = "http://cork.firelet.net/",
    long_description = "Cork is a simple Authentication/Authorization library" \
        "for the Bottle web framework.",
    classifiers=CLASSIFIERS,
    install_requires = [
        'bottle',
        'beaker',
    ],
    modules = ["cork"],
    platforms = ['Linux'],
    package_data = {
        '': [
            'test/*',
            'cork.py',
            'examples/*'
        ]
    },
    entry_points = {},
    scripts = ([]),
    test_suite='nose.collector',
    tests_require=['nose'],
)

