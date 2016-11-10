#!/usr/bin/python

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

import argparse
def getArgs():
    p=argparse.ArgumentParser(
            description="Download a webcomic archive"
            )
    p.add_argument("comic",
            help="the name or URL of the webcomic to comic download"
            )
    p.add_argument("-n", "--max",
            dest="max",
            metavar="n",
            default=0,
            type=int,
            help="Maximum number of comics to download. 0 means unlimited"
            )
    p.add_argument("-f", "--from-url",
            dest="fromURL",
            action="store_true",
            help="By default, webcomic-dl will download from the first webcomic in the series, regardless of the URL. This flag overrides it. For some comics that don't have numbers associated with their comics, this may cause naming collisions if you later decide to go back and download older comics. Thus, only use this if you are either certain you will never want earlier comics, or are willing to re-download the newer ones."
            )
    p.add_argument("-d", "--dir",
            dest="directory",
            metavar="dir",
            default="",
            help="Specify an output directory"
            )
    p.add_argument("-o", "--overwrite",
            dest="overwrite",
            action="store_true",
            help="Force overwriting of downloaded comics. By default, webcomic-dl will not overwrite already-downloaded comics."
            )
    p.add_argument("--no-resume",
            dest="resume",
            action="store_false",
            help="By default, webcomic-dl will resume downloads from where it last left off. This flag overrides it. Does not download already-downloaded comics unless -o is also used, but still needs to download the webpage of each comic"
            )
    p.add_argument("-m" "--metadata-file",
            dest="file",
            help="Specify where to save metadata. By default it is saved in <output_dir>/info.json",
            metavar="file"
            )
    p.add_argument("--metadata-only",
            dest="meta",
            action="store_true",
            help="Don't download comics, just metadata"
            )
    p.add_argument("-c", "--compact",
            dest="pretty",
            action="store_false",
            help="Disable pretty-printing the output JSON, if you're really trying to save some bytes"
            )
    p.add_argument("-i", "--index",
            dest="html",
            action="store_true",
            help="Places an HTML-based viewer called index.html in the output directory"
            )
    p.add_argument("-v", "--verbose",
            dest="verbose",
            action="store_true",
            help="Be verbose. Mostly for testing purposes"
            )
    return p.parse_args()
