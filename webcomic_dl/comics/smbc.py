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
class SmbcComic(Comic):
    nextSelector="a.next"
    titleSelector="title"
    imgSelector="#cc-comic"
    bonusSelector="#aftercomic > img"
    siteTitle="Saturday Morning Breakfast Cereal"
    directory="SMBC"
    urlRegex="^https?://(?:www\.)?smbc-comics\.com(?:/|$)"
    name="smbc"
    first="http://www.smbc-comics.com/comic/2002-09-05"

    def getTitle(self):
        return re.search(r'^Saturday Morning Breakfast Cereal - (.*)$', super().getTitle()).groups(1)[0]

    def getNumber(self):
        if(self.number is None):
            print("downloading index")
            page=Webpage("http://smbc-comics.com/comic/archive")
            elements=page.getElements("select[name='comic'] > option")
            for i, e in enumerate(elements):
                if(self.url.rstrip("/").endswith("/" + e.attrib["value"])):
                    self.number=i
                    break
        return self.number
