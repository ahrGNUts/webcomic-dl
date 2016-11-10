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
class QuestionableContentComic(Comic):
    nextSelector="#comicnav li:nth-child(3) a"
    titleSelector=False
    imgSelector="#strip"
    siteTitle="Questionable Content"
    directory="Questionable Content"
    urlRegex="^https?://(?:www\.)?questionablecontent\.net(?:/|$)"
    name="questionable-content"
    first="https://questionablecontent.net/view.php?comic=1"
    textSelector="#news"
    def getNumber(self):
        return int(re.search(r'comic=(\d+)', self.url).group(1))
