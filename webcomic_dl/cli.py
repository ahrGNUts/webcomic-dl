#!/usr/bin/python
import argparse
def getArgs():
	p=argparse.ArgumentParser(
			description="Download a webcomic archive"
			)
	p.add_argument("comic",
			help="the name or URL of the webcomic to comic download"
			)
	p.add_argument("-c", "--count",
			dest="max",
			metavar="n",
			default=0,
			type=int,
			help="Maximum number of comics to download. 0 means unlimited"
			)
	p.add_argument("-f", "--from-url",
			help="By default, webcomic-dl will download from the first webcomic in the series, regardless of the URL. This flag overrides it. For some comics that don't have numbers associated with their comics, this may cause naming collisions if you later decide to go back and download older comics. Thus, only use this if you are either certain you will never want earlier comics, or are willing to re-download the newer ones."
			dest="from",
			action="store_true",
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
                        help="By default, webcomic-dl will resume downloads from where it last left off. This flag overrides it. Does not download already-downloaded comics unless -o is also used, but still needs to download the webpage of each comic"
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
