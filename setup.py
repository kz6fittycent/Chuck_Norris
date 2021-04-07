#!/usr/bin/env python3

from setuptools import setup

setup(
    name="chucknorris",
    version="1.3",
    description="Chuck Norris jokes right from your terminal",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libchucknorris"],
    scripts=["chucknorris"],
    package_data={"libchucknorris": ["data/*"]},
)
