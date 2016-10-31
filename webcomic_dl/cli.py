#!/usr/bin/python
import argparse
def getArgs():
	p=argparse.ArgumentParser(
			description="Download a webcomic archive"
			)
	p.add_argument("url",
			help="the URL of the webcomic to comic download"
			)
	p.add_argument("-n", "--max",
			dest="max",
			metavar="n",
			default=0,
			type=int,
			help="Maximum number of comics to download. 0 means unlimited"
			)
	p.add_argument("-d", "--dir",
			dest="dir",
			metavar="dir",
			default="",
			help="Specify an output directory"
			)
	p.add_argument("-o", "--overwrite",
			dest="overwrite",
			action="store_true",
			help="Force overwriting of downloaded comics. By default, webcomic-dl will not overwrite already-downloaded comics."
			)
        p.add_argument("-n", "--no-resume",
                        dest="resume",
                        action="store_false",
                        help="By default, webcomic-dl will resume downloads from where it last left off. This flag overrides it. Still does not download already-downloaded comics unless combined with -o."
	p.add_argument("-f", "--file",
			dest="file",
			help="Specify where to save metadata. By default it is saved in <output_dir>/info.json",
			metavar="file"
			)
	p.add_argument("-m", "--metadata-only",
			dest="meta",
			action="store_true",
			help="Don't download comics, just metadata"
			)
	return p.parse_args()
