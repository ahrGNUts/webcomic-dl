import requests
import re
from lxml import html
from lxml.cssselect import CSSSelector
from urllib.parse import urljoin
import os.path
import os
import json

class Comic:
    #the CSS selector for the "next" link
    nextSelector=None
    #the CSS selector for the comic title
    titleSelector=None
    #the CSS selector for the comic img
    imgSelector=None
    #the CSS selector for supplemental text
    siteTitle=None
    #the default directory name to download into
    defaultDirname="comics"
    #the regex for matching the URL to the Comic
    urlRegex=".*"
    #comic name
    name=""
    #url of first comic
    first=""
    #headers to use for the request
    headers={}
    @classmethod
    def match(cls, s:str):
        """Returns whether this Comic class will work for the given URL"""
        if s==cls.name:
            return cls.first
        elif re.search(cls.urlRegex, s):
            return s
        return False

    def __init__(self, url:str=None, number:int=1):
        """Creates a Comic object, downloads and parses the comic page"""
        self.url=self.__class__.match(url)
        txt=requests.get(self.url, headers=self.headers).text
        self.dom=html.fromstring(txt)
        self.number=number
    
    def _getElement(self, selector:str):
        if not selector:
            return None
        sel=CSSSelector(selector)
        e=sel(self.dom)
        if(len(e)):
            return e[0]
        return None

    def _getAttr(self, selector:str, attr:str):
        """Return the value of the given attribute for the first element matching the given selector"""
        e=self._getElement(selector)
        if(e is not None and attr in e.attrib):
            return e.attrib[attr]
        else:
            return ""

    def _getText(self, selector:str):
        """Return the text of the first element matching the given selector"""
        e=self._getElement(selector)
        if(e is not None):
            return e.text
        else:
            return ""

    def getNumber(self):
        """
        Return the page number
        
        Most subclasses will want to override this with something that extracts
        the number from the webpage or URL
        """
        return self.number

    def getTitle(self):
        """Return the title of this comic"""
        return self._getText(self.titleSelector)

    def getImg(self):
        """Return the image URL for this page"""
        return urljoin(
                self.url,
                self._getAttr(self.imgSelector, "src")
                )

    def getImgExtension(self):
        """Return the filename extension for the image"""
        return re.search(r'\.([a-zA-Z]+)$', self.getImg()).group(1)

    def getImgFilename(self):
        """Return the filename to save the image as"""
        parts=[str(self.getNumber()).zfill(6)]
        if(self.getTitle()):
            parts.append(self.getTitle())
        return (" - ".join(parts)) + "." + self.getImgExtension()

    def getAlt(self):
        """Return the alt text for this comic"""
        return self._getAttr(self.imgSelector, "alt")

    def getNextURL(self):
        """Return the URL of the next page if there is one, or False otherwise"""
        url=self._getAttr(self.nextSelector, "href")
        if(url):
            return urljoin(self.url, url)
        return None

    def hasNext(self):
        """Return whether there is another comic after this one"""
        return self.getNextURL() is not None

    def getNextComic(self):
        """Return a Comic object corresponding to the next comic"""
        url=self.getNextURL()
        if(url is not None):
            return self.__class__(url, None if self.number is None else self.number+1)
        return None
    
    def toDict(self):
        """Return a dict with all the important stuff"""
        return {
                "number": self.getNumber(),
                "title": self.getTitle(),
                "url": self.url,
                "imgurl": self.getImg(),
                "imgfile": self.getImgFilename(),
                "alt": self.getAlt()
                }
    
    def dir(self, dirname:str=None):
        d=dirname or self.defaultDirname
        if(not os.path.isdir(d)):
            os.mkdir(d)
        return d

    def downloadImg(self, dirname:str=None, overwrite=False):
        """Download the image, saving it in the specified directory. Saves under a different name and then moves it, to improve integrity"""
        d=self.dir(dirname)
        filename=os.path.join(d, self.getImgFilename())
        tmpfile=os.path.join(d, self.getImgFilename()+".incomplete")
        if(not overwrite and os.path.isfile(filename)):
            return False
        if(os.path.isfile(tmpfile)):
            os.remove(tmpfile)
        r=requests.get(self.getImg(), stream=True)
        with open(tmpfile, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if(chunk):
                    f.write(chunk)
        if(os.path.isfile(tmpfile)):
            os.rename(tmpfile, filename)
        return filename
    
    def saveProgress(self, dirname:str=None):
        """Save where we've left off"""
        d=self.dir(dirname)
        tmpfile=os.path.join(d, ".progress.tmp")
        filename=os.path.join(d, ".progress")
        with open(tmpfile, "w") as f:
            f.write(json.dumps({
                "url": self.url,
                "num": self.getNumber()
                }))
        if(os.path.isfile(tmpfile)):
            os.rename(tmpfile, filename)
