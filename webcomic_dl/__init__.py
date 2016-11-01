import requests
import re
from lxml import html
from lxml.cssselect import CSSSelector
from urllib.parse import urljoin
import os.path
import os
import json

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
    """the CSS selector for supplemental text"""
    defaultDirname="comics"
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

    floating=True
    """
    Keeps track of whether anything links the number field to the canonical
    numbering scheme of the comic. Subclasses should check this in getNumber(),
    and only perform expensive checks on numbering if this field is True. After
    performing the checks and establishing the link, they should unset this
    field.
    """
    
    dom=None
    """
    The DOM of the webpage for this comic
    """
    @classmethod
    def match(cls, s:str):
        """Returns whether this Comic class will work for the given URL"""
        if s==cls.name:
            return cls.first
        elif re.search(cls.urlRegex, s):
            return s
        return False
    @classmethod
    def getDOM(cls, url:str):
        """Returns a parsed DOM of the webpage of a URL"""
        txt=requests.get(url, headers=cls.headers).text
        return html.fromstring(txt)

    def __init__(self, url:str=None, number:int=1, floating:bool=True):
        """Creates a Comic object, downloads and parses the comic page"""
        self.url=self.match(url)
        self.floating = floating and (self.url!=self.first) #if the URL points to the first comic, it's not "floating"
        self.number=number
    
    def load(self):
        """Downloads the webpage. Prett important for most of the stuff in this class"""
        if(self.dom is None):
            print("Downloading webpage {0}".format(self.url))
            self.dom=self.getDOM(self.url)

    def _getElements(self, selector:str, dom=None):
        """Return all elements matching the given selector"""
        self.load()
        d=dom if(dom is not None) else self.dom
        if not selector:
            return None
        sel=CSSSelector(selector)
        e=sel(d)
        return e

    def _getElement(self, selector:str, dom=None):
        """Return the first element matching the given selector"""
        e=self._getElements(selector, dom)
        if(e is not None and len(e)):
            return e[0]
        return None

    def _getAttr(self, selector:str, attr:str, dom=None):
        """Return the value of the given attribute for the first element matching the given selector"""
        e=self._getElement(selector, dom)
        if(e is not None and attr in e.attrib):
            return e.attrib[attr]
        else:
            return ""

    def _getText(self, selector:str, dom=None):
        """Return the text of the first element matching the given selector"""
        e=self._getElement(selector, dom)
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
        imgurl=self._getAttr(self.imgSelector, "src")
        if(imgurl):
            return urljoin(
                    self.url,
                    imgurl
                    )
        return None

    def getImgExtension(self, img=None):
        """Return the filename extension for the image"""
        i=img or self.getImg()
        if(i):
            return re.search(r'\.([a-zA-Z]+)$', i).group(1)
        return None

    def getImgFilename(self, suffix:str="", extension:str=None):
        """Return the filename to save the image as"""
        if(self.getImg()):
            ext=extension or self.getImgExtension()
            parts=[str(self.getNumber()).zfill(6)]
            if(self.getTitle()):
                parts.append(self.getTitle())
            out=(" - ".join(parts)) + suffix + "." + ext
            return re.sub(r'[/\\]', '_', out)
        return None

    def getBonusImg(self):
        if(self.bonusSelector):
            return self._getAttr(self.bonusSelector, "src")
        return None
        
    def getBonusImgFilename(self):
        img=self.getBonusImg()
        if(img):
            return self.getImgFilename(".bonus", self.getImgExtension(img))
        return None

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

    def getNextComic(self, url:str=None):
        """Return a Comic object corresponding to the next comic"""
        url=url or self.getNextURL()
        if(url is not None):
            return self.__class__(
                    url      = url,
                    number   = None if self.number is None else self.number+1,
                    floating = self.floating)
        return None
    
    def toDict(self):
        """Return a dict with all the important stuff"""
        d={
                "url": self.url
                }
        if(self.getTitle()):
            d["title"]=self.getTitle()
        if(self.getImgFilename()):
            d["img"]=self.getTitle()
        if(self.getAlt()):
            d["alt"]=self.getAlt()
        if(self.getBonusImgFilename()):
            d["bonus"]=self.getBonusImgFilename()
        return d
    
    def dir(self, dirname:str=None):
        d=dirname or self.defaultDirname
        if(not os.path.isdir(d)):
            os.mkdir(d)
        return d

    def download(self, dirname:str=None, overwrite=False):
        """Download the image, saving it in the specified directory. Saves under a different name and then moves it, to improve integrity"""
        d=self.dir(dirname)
        if(self.getImg()):
            self.downloadImage(
                    os.path.join(d, self.getImgFilename()),
                    self.getImg(),
                    overwrite
                    )
        if(self.getBonusImg()):
            self.downloadImage(
                    os.path.join(d, self.getBonusImgFilename()),
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
