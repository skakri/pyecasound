# coding=utf-8

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyecasound",
    version="dev",
    author="Kristaps Karlsons",
    description=("Ecasound is a software package designed for "
                 "multitrack audio processing"),
    license="LGPL",
    keywords="ecasound pyecasound",
    url="https://github.com/skakri/ecasound/tree/devel-python3",
    package_dir={'': 'ecasound/pyecasound'},
    py_modules=[
        'eci',
        'pyeca',
        'ecacontrol',
    ],
    # long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 "
        "or later (LGPLv2+)",
        "Topic :: Multimedia :: Sound/Audio",
    ],
)
