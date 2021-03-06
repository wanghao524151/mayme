#!/usr/bin/env python
#-*- coding:utf-8 -*-

from distutils.core import setup
import glob
import py2exe


setup(
    name='program',
    options={"py2exe": {"compressed": 1, "optimize": 2, "ascii": 0, "bundle_files": 1}},
    zipfile=None,
    windows=[{'script': 'MayMe.py'}],
    data_files=[
        ("demo_source", ["demo_source/beijing.xls", "demo_source/hunan.xls", "demo_source/material.xls"]),
    ],
)
