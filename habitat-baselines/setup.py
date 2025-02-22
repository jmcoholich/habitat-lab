#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import glob
import os.path
import sys

import setuptools
from setuptools.command.develop import develop as DefaultDevelopCommand
from setuptools.command.install import install as DefaultInstallCommand

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "habitat_baselines")
)
from version import VERSION  # isort:skip noqa


with open("../README.md", encoding="utf8") as f:
    readme = f.read()


DISTNAME = "habitat-baselines"
DESCRIPTION = "Habitat baselines: a modular high-level library for end-to-end development in Embodied AI training."
LONG_DESCRIPTION = readme
AUTHOR = "Facebook AI Research"
LICENSE = "MIT License"
DEFAULT_EXCLUSION = ["tests"]
URL = "https://aihabitat.org/"
PROJECT_URLS = {
    "GitHub repo": "https://github.com/facebookresearch/habitat-lab/",
    "Bug Tracker": "https://github.com/facebookresearch/habitat-lab/issues",
}
REQUIREMENTS = set()
# collect requirements.txt file in all subdirectories
for file_name in glob.glob(
    "habitat_baselines/**/requirements.txt", recursive=True
):
    with open(file_name) as f:
        reqs = f.read()
        REQUIREMENTS.update(reqs.strip().split("\n"))

if __name__ == "__main__":
    setuptools.setup(
        name=DISTNAME,
        install_requires=list(REQUIREMENTS),
        packages=setuptools.find_packages(exclude=DEFAULT_EXCLUSION),
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author=AUTHOR,
        license=LICENSE,
        setup_requires=["pytest-runner"],
        tests_require=[
            "pytest-cov",
            "pytest-mock",
            "pytest",
            "pybullet==3.0.4",
            "mock",
        ],
        include_package_data=True,
        cmdclass={
            "install": DefaultInstallCommand,
            "develop": DefaultDevelopCommand,
        },
        url=URL,
        project_urls=PROJECT_URLS,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Development Status :: 5 - Production/Stable",
            "License :: OSI Approved :: MIT License",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Operating System :: MacOS",
            "Operating System :: Unix",
        ],
        entry_points={
            "console_scripts": [
                "habitat-baselines=habitat_baselines.run:main",
            ],
        },
    )
