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
from webcomic_dl.webpage import Webpage
import re
class HarkAVagrantComic(Comic):
    nextSelector='table td[colspan="2"] > center:first-child a:nth-child(3)'
    imgSelector='table td[colspan="2"] > center > .rss-content > img'
    siteTitle="Hark! A Vagrant"
    directory="Hark! A Vagrant"
    urlRegex='^https?://(?:www\.)?harkavagrant\.com(?:/|$)'
    name="harkavagrant"
    first="http://www.harkavagrant.com/index.php?id=1"
    textSelector=".black11 .rss-content"
    printSelector='table td[colspan="2"] > center:last-child a:last-child'

    def getTitle(self):
        return self.getAlt()

    def getNumber(self):
        return int(re.search(r'\d+$', self.url).group(0))
