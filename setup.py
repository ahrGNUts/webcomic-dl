#!/usr/bin/env python

#Copyright 2016 Devon Sawatzky

#This file is part of webcomic-dl.

#webcomic-dl is free software: you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software
#Foundation, either version 3 of the License, or (at your option) any later
#version.

#webcomic-dl is distributed in the hope that it will be useful, but WITHOUT ANY
#WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#PARTICULAR PURPOSE.  See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with
#webcomic-dl.  If not, see <http://www.gnu.org/licenses/>.

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
