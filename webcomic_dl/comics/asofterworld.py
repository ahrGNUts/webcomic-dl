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

from webcomic_dl import Comic
import re

class ASofterWorldComic(Comic):
    nextSelector='#next a'
    """the CSS selector for the "next" link"""
    imgSelector='#comicimg img'
    """the CSS selector for the comic img"""
    siteTitle='A Softer World'
    """The Site's Title"""
    directory='A Softer World'
    """the default directory name to download into"""
    urlRegex="^https?://(?:www\.)?asofterworld\.com(?:/|$)"
    """the regex for matching the URL to the Comic"""
    name="asofterworld"
    """Name of the comic"""
    first="http://www.asofterworld.com/index.php?id=1"
    """URL of first comic"""
    textSelector='#wholenewsbox'
    """the CSS selector for supplemental text"""
    printSelector='#buyprint a'
    """the CSS selector for the "Buy this as a print" link"""
