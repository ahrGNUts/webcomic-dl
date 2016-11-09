#webcomic-dl

Download the archives of a webcomic for offline reading

```
usage: webcomic-dl [-h] [-n n] [-f] [-d dir] [-o] [--no-resume]
                   [-m--metadata-file file] [--metadata-only] [-c] [-i] [-v]
                   comic

Download a webcomic archive

positional arguments:
  comic                 the name or URL of the webcomic to comic download

optional arguments:
  -h, --help            show this help message and exit
  -n n, --max n         Maximum number of comics to download. 0 means
                        unlimited
  -f, --from-url        By default, webcomic-dl will download from the first
                        webcomic in the series, regardless of the URL. This
                        flag overrides it. For some comics that don't have
                        numbers associated with their comics, this may cause
                        naming collisions if you later decide to go back and
                        download older comics. Thus, only use this if you are
                        either certain you will never want earlier comics, or
                        are willing to re-download the newer ones.
  -d dir, --dir dir     Specify an output directory
  -o, --overwrite       Force overwriting of downloaded comics. By default,
                        webcomic-dl will not overwrite already-downloaded
                        comics.
  --no-resume           By default, webcomic-dl will resume downloads from
                        where it last left off. This flag overrides it. Does
                        not download already-downloaded comics unless -o is
                        also used, but still needs to download the webpage of
                        each comic
  -m--metadata-file file
                        Specify where to save metadata. By default it is saved
                        in <output_dir>/info.json
  --metadata-only       Don't download comics, just metadata
  -c, --compact         Disable pretty-printing the output JSON, if you're
                        really trying to save some bytes
  -i, --index           Places an HTML-based viewer called index.html in the
                        output directory
  -v, --verbose         Be verbose. Mostly for testing purposes
```
