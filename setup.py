#!/usr/bin/env python3
import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst"), "r") as fid:
    long_description = fid.read()

setup(
    name = "pandoc-div2env",
    version = "1.0",

    description = "Convert Pandoc Div to LaTeX environemt",
    long_description = long_description,
    keywords = "pandoc, filter, latex, environment",

    author = "Keith F Prussing",
    author_email = "kprussing74@gmail.com",
    maintainer = "Keith F Prussing",
    maintainer_email = "kprussing74@gmail.com",

    url = "https://github.com/kprussing/pandoc-div2env",
    dowload_url = "https://github.com/kprussing/pandoc-div2env/releases",
    license = "MIT",

    install_requires = ["panflute >= 1.11.0"],

    py_modules = ["pandiv2env"],
    entry_points = {
        "console_scripts" : {
            "pandoc-div2env = pandiv2env:main",
        },
    },

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Filters',
    ],
)

