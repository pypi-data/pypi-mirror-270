#!/usr/bin/env python
# coding:utf-8
import os
from setuptools import setup, find_packages

setup(
    name='vio',
    version='0.0.0.2',
    description='virtual io ...',
    long_description="I'm trying to make a virtual io for python object getter.",
    author_email='2229066748@qq.com',
    maintainer="Eagle'sBaby",
    maintainer_email='2229066748@qq.com',
    packages=find_packages(),
    # package_data={
    #     '': ['*.7z'],
    # },
    license='Apache Licence 2.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'pyscreeps-arena=pyscreeps_arena:CMD_NewProject',
    #     ]
    # },
    keywords=['python'],
    # python_requires='>=3.10',
    # install_requires=[
    #     'pyperclip',
    #     'colorama',
    #     'py7zr',
    #     'Transcrypt==3.9.1',
    #     'mkdocs',
    #     'mkdocstrings[python]',
    #     'mkdocs-material',
    # ],
)
