#!/usr/bin/env python
# setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MacroMancer",
    version="0.0.1",
    author="Alexander N. Shelton",
    author_email="alexander.nathan.shelton@outlook.com",
    description="A CLI application for managing keyboard and mouse bindings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alexander-N-Shelton/MacroMancer",
    packages=setuptools.find_packages(),
    package_dir={"": "."},                 
    install_requires=[
        "pyfiglet",
        "rich",
        "InquirerPy",
        "PyYaml", 
        "pynput"
    ],

    entry_points = {
        "console_scripts": [
            "macromancer=macromancer.main:main",
        ]
    },
        classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience  :: Linux Users",
        "Topic :: Key/Mouse Bindings and Macros",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires=">=3.10, <3.13",
    package_data={
        'macromancer': ['docs/*.md', 'config/*.yaml'],
    },
    include_package_data=True,
)
