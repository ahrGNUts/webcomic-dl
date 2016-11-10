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
class XkcdComic(Comic):
    nextSelector="a[rel=next]"
    titleSelector="#ctitle"
    imgSelector="#comic img"
    siteTitle="xkcd"
    directory="xkcd"
    urlRegex="^https?://xkcd\.com(?:/|$)"
    name="xkcd"
    first="https://xkcd.com/1"
    def getNumber(self):
        return int(re.search(r'\d+', self.url).group(0))
