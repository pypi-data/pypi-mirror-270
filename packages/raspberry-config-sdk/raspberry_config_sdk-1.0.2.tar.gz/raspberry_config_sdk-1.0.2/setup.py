#!/usr/bin/env python3
#  Copyright (c) 2023.
#  All rights reserved to the creator of the following script/program/app, please do not
#  use or distribute without prior authorization from the creator.
#  Creator: Antonio Manuel Nunes Goncalves
#  Email: amng835@gmail.com
#  LinkedIn: https://www.linkedin.com/in/antonio-manuel-goncalves-983926142/
#  Github: https://github.com/DEADSEC-SECURITY

from setuptools import find_packages, setup
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text(encoding="utf8")

setup(
    name="raspberry-config-sdk",
    packages=find_packages(),
    version="1.0.2",
    description="Easily Configure your Raspberry Pi from your code",
    long_description=README,
    long_description_content_type="text/markdown",
    author="DeadSec-Security",
    author_email="amng835@gmail.com",
    url="https://github.com/DEADSEC-SECURITY/raspberry-config-sdk",
    install_requires=["tqdm~=4.66.0", "bigtree~=0.17.0"],
    keywords=["raspberry", "raspberry pi", "config.txt", "raspberry config", "boot"],
    license="MIT",
    python_requires=">=3.8,==3.11.2",
)
