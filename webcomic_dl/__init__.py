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

import requests
import re
from lxml import html, etree
from lxml.cssselect import CSSSelector
from urllib.parse import urljoin
import os.path
import os
import json
from webcomic_dl.webpage import Webpage
import sys

htmlFile=os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "index.html")

class Comic:
    nextSelector=None
    """the CSS selector for the "next" link"""
    titleSelector=None
    """the CSS selector for the comic title"""
    imgSelector=None
    """the CSS selector for the comic img"""
    bonusSelector=None
    """the CSS selector for the bonus img"""
    siteTitle=None
    """The Site's Title"""
    textSelector=None
    """the CSS selector for supplemental text"""
    printSelector=None
    """the CSS selector for the "Buy this as a print" link"""
    directory="comics"
    """the default directory name to download into"""
    urlRegex=".*"
    """the regex for matching the URL to the Comic"""
    name=""
    """Name of the comic"""
    first=""
    """URL of first comic"""
    headers={}
    """
    Specifies headers to use for all the web requests.

    May be used in the future for authentication or useragent strings.
    """
    encoding=None
    """The character encoding of this comic's website"""
    extension=None
    """The file extension of this comic's images"""

    page=None
    """The Webpage for this comic"""

    @classmethod
    def match(cls, s:str):
        """Returns whether this Comic class will work for the given URL"""
        if s==cls.name:
            return cls.first
        elif re.search(cls.urlRegex, s):
            return s
        return False

    def __init__(self, url=None, number:int=None, blank:bool=False):
        """Creates a Comic object"""
        if(not blank):
            self.url=self.match(url)
        if(number is not None):
            self._number=number
        elif(self.url==self.first):
            self._number=1
        else:
            self._number=None

    def setDir(self, directory):
        self.directory=directory

    def load(self):
        """
        Downloads the webpage.

        Pretty important for most of the stuff in this class
        """
        if(self.page is None):
            print("Downloading webpage {0}".format(self.url))
            self.page=Webpage(self.url, headers=self.headers, encoding=self.encoding)

    @property
    def number(self):
        if(self._number is None):
            self._number=self.getNumber()
        return self._number

    def getNumber(self):
        """
        Return the page number

        Subclasses need to override this with something that extracts the
        number from the webpage or URL. As these methods can be expensive
        (downloading index pages, etc) it's memoized behind the 'number'
        @property
        """
        raise NotImplementedError("This comic must be downloaded from the first page!")

    def getTitle(self):
        """Return the title of this comic"""
        self.load()
        return self.page.getText(self.titleSelector)

    def getImg(self):
        """Return the image URL for this page"""
        self.load()
        return self.page.getURL(self.imgSelector, "src")

    def getPrintURL(self):
        """Get the URL to buy a print of the comic from the artist. SUPPORT ARTISTS!"""
        return self.page.getURL(self.printSelector)

    def getBonusImg(self):
        """Return the bonus image URL for this page"""
        self.load()
        if(self.bonusSelector):
            return self.page.getURL(self.bonusSelector, "src")
        return None

    def getFileExtension(self, url:str):
        """Return the filename extension for the image"""
        if(self.extension):
            return self.extension
        if(url):
            parts=url.split(".")
            if(len(parts) > 1):
                return parts[-1]
        return None

    def imgFilename(self, url, number, title="", suffix=""):
        ext=self.getFileExtension(url)
        num="{0}".format(number).zfill(6)
        if(title):
            name="{0} - {1}{2}.{3}".format(num, title, suffix, ext)
        else:
            name="{0}{1}.{2}".format(num, suffix, ext)
        return re.sub(r'[/\\]', '_', name)

    def getImgFilename(self, suffix:str=""):
        """Return the filename to save the image as"""
        img=self.getImg()
        if(img):
            return self.imgFilename(img, self.number, self.getTitle())
        return None

    def getBonusImgFilename(self, suffix:str=""):
        """Return the filename to save the bonus image as"""
        img=self.getBonusImg()
        if(img):
            return self.imgFilename(img, self.number, self.getTitle(), ".bonus")
        return None

    def getSupplementalText(self):
        self.load()
        if(self.textSelector):
            return self.page.getText(self.textSelector)
        else:
            return None

    def getAlt(self):
        """Return the alt text for this comic"""
        self.load()
        return self.page.getAttr(self.imgSelector, "title")

    def getNextURL(self):
        """Return the URL of the next page if there is one, or False otherwise"""
        self.load()
        return self.page.getURL(self.nextSelector)

    def hasNext(self):
        """Return whether there is another comic after this one"""
        url=self.getNextURL()
        return (url is not None) and (url.rstrip("/#") != self.url.rstrip("/#"))

    def getNextComic(self, url:str=None, blank:bool=False):
        """Return a Comic object corresponding to the next comic"""
        if(blank or url or self.hasNext()):
            comic=self.__class__(
                    url      = url or blank or self.getNextURL(),
                    number   = None if self._number is None else self._number+1,
                    blank    = blank
                    )
            comic.setDir(self.directory)
            return comic
        return None

    def toDict(self):
        """Return a dict with all the important stuff"""
        d={
                "url": self.url
                }
        if(self.getTitle()):
            d["title"]=self.getTitle()
        if(self.getImgFilename()):
            d["img"]=self.getImgFilename()
        if(self.getAlt()):
            d["alt"]=self.getAlt()
        if(self.getBonusImgFilename()):
            d["bonus"]=self.getBonusImgFilename()
        if(self.getSupplementalText()):
            d["text"]=self.getSupplementalText()
        if(self.getPrintURL()):
            d["print"]=self.getPrintURL()
        return d

    def download(self, dirname:str=None, overwrite=False):
        """Download the image, saving it in the specified directory. Saves under a different name and then moves it, to improve integrity"""
        if(not os.path.isdir(self.directory)):
            os.mkdir(self.directory)
        if(self.getImg()):
            self.downloadImage(
                    os.path.join(self.directory, self.getImgFilename()),
                    self.getImg(),
                    overwrite
                    )
        if(self.getBonusImg()):
            self.downloadImage(
                    os.path.join(self.directory, self.getBonusImgFilename()),
                    self.getBonusImg(),
                    overwrite
                    )

    def downloadImage(self, filename:str, url:str, overwrite=False):
        tmpfile=filename+".incomplete"
        if(not overwrite and os.path.isfile(filename)):
            return False
        if(os.path.isfile(tmpfile)):
            os.remove(tmpfile)
        print("Downloading image   {0}".format(filename))
        r=requests.get(url, stream=True)
        with open(tmpfile, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if(chunk):
                    f.write(chunk)
        if(os.path.isfile(tmpfile)):
            os.rename(tmpfile, filename)
        return filename
