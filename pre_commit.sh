#!/bin/bash
. virtualenv/bin/activate
cat README.pre > README.md
echo -e '\n```' >> README.md
webcomic-dl --help >> README.md
echo '```' >> README.md
git update-index --add README.md
