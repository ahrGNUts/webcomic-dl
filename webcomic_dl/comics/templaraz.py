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
class TemplarAZComic(Comic):
    nextSelector="a[rel=next]"
    imgSelector="#comic > img"
    siteTitle="Templar, Arizona"
    directory="Templar, Arizona"
    urlRegex=r'^((?:.+[/\.])?templaraz\.com)(/|$)'
    name="templaraz"
    first="http://templaraz.com/2005/05/26/chapter-1-the-great-outdoors-cover/"
    firstSelector=".nav-first > a"
    
    def getNumber(self):
        self.load()
        if(self.page.getElement(self.firstSelector) is None):
            return 1;
        else:
            super().getNumber()
