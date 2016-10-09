#!/usr/bin/env python

from distutils.core import setup

setup(name="webcomic-dl",
        version="0.1",
        description="Webcomic archive downloader",
        author="Devon Sawatzky",
        author_email="d@dn3s.me",
        url="https://dn3s.me/projects/webcomic-dl",
        package_dir={"webcomic_dl": "lib"},
        packages=["webcomic_dl.extractor",
            "webcomic_dl.downloader"
            ],
        requires=["requests", "progress"],
        scripts=["bin/webcomic-dl"]
        )
