#!/bin/bash
. virtualenv/bin/activate
cat README.pre > README.md
webcomic-dl --help >> README.md
git update index --add README.md
