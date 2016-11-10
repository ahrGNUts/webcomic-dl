#webcomic-dl

Download the archives of a webcomic for offline reading.

This is my first Python project, so things may be a little rough for a while,
particularly the install process, but I'm learning fast!

One nice thing about this program is it does all of the scraping with CSS
selectors, so it's really easy to add support for a new comic!

All info on this page is written only with Linux in mind. The code itself
should be fairly portable, and the installation should be relatively
generic for a Python project, but I cannot offer any guidance on non-linux
platforms. Feel free to share your experiences though!

##Requirements

This was written specifically for Python 3, so make sure you have `python3` 
installed. At this point, I would recommend installing in a `virtualenv` so
make sure that's installed as well.

##Installation

I may submit this to the Python Package Archive if I radically clean this up.
But for now:

```
git clone 'https://github.com/dn3s/webcomic-dl.git'
cd webcomic-dl
./setup.py install
```

I'm still learning about packaing and distribution, so for now you may want to
do this in a `virtualenv`. There's a `.gitignore` entry for a directory called
`virtualenv`, so you can set it up there for painless updates:

```
git clone 'https://github.com/dn3s/webcomic-dl.git'
cd webcomic-dl
virtualenv -p python3 virtualenv
. virtualenv/bin/activate
./setup.py develop
```

Then when you want to use it, make sure you activate the virtualenv with
`. <path_to_webcomic-dl>/virtualenv/bin/activate`.

##Contributing

If anyone has advice on overall design and architecture, I'd love to hear it!
If you want to add support for your favorite webcomic, take a look at
`webcomic_dl/comics`; I'll document it more thoroughly soon.

If you want to contribute directly, it's probably wise to setup a `virtualenv`,
and please install the pre-commit hook (`cp pre_commit.sh
.git/hooks/pre-commit`)

One other note, if you want to edit this README, edit `README.pre`, as
`README.md` is overwritten by the pre-commit hook.

Pull requests welcome!

##Issues/TODO

The program is perfectly usable now, but still needs some work for to improve
maintainability:

- Main control logic needs refactoring
- Module layout is a little wonky. `Comic` should not be in
  `webcomic_dl/__init__.py`
- HTML viewer needs a heavy refactor/total rewrite; the code is very much a
  quick hack
- Clean up existing comments, docstrings, thouroughly document how to add comic
  support, format existing comics consistently, create a starting template for
  people to copy
- Prettier progress display

##Usage

```
usage: webcomic-dl [-h] [-n <n>] [-f] [-d <dir>] [-o] [--no-resume]
                   [-m <file>] [--metadata-only] [-c] [-i] [-v]
                   comic

Download a webcomic archive

positional arguments:
  comic                 the name or URL of the webcomic to comic download

optional arguments:
  -h, --help            show this help message and exit
  -n <n>, --max <n>     Maximum number of comics to download. 0 means
                        unlimited
  -f, --from-url        By default, webcomic-dl will download from the first
                        webcomic in the series, regardless of the URL. This
                        flag overrides it. For some comics that don't have
                        numbers associated with their comics, this may cause
                        naming collisions if you later decide to go back and
                        download older comics. Thus, only use this if you are
                        either certain you will never want earlier comics, or
                        are willing to re-download the newer ones.
  -d <dir>, --dir <dir>
                        Specify an output directory
  -o, --overwrite       Force overwriting of downloaded comics. By default,
                        webcomic-dl will not overwrite already-downloaded
                        comics.
  --no-resume           By default, webcomic-dl will resume downloads from
                        where it last left off. This flag overrides it. Does
                        not download already-downloaded comics unless -o is
                        also used, but still needs to download the webpage of
                        each comic
  -m <file>, --metadata-file <file>
                        Specify where to save metadata. By default it is saved
                        in <output_dir>/info.json
  --metadata-only       Don't download comics, just metadata
  -c, --compact         Disable pretty-printing the output JSON, if you're
                        really trying to save some bytes
  -i, --index           Places an HTML-based viewer called index.html in the
                        output directory
  -v, --verbose         Be verbose. Mostly for testing purposes
```
