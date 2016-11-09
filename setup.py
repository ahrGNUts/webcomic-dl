#!/usr/bin/env python

from setuptools import setup

setup(name="webcomic-dl",
        version="0.1",
        description="Webcomic archive downloader",
        author="Devon Sawatzky",
        author_email="d@dn3s.me",
        url="https://dn3s.me/projects/webcomic-dl",
        packages=["webcomic_dl", "webcomic_dl.comics"],
        install_requires=["requests", "progress", "cssselect", "lxml"],
        scripts=["bin/webcomic-dl"],
        package_data={"webcomic_dl": ["data/index.html"]}
        )
