import requests
import re
from lxml import html, etree
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
    """The Site's Title"""
    textSelector=None
    """the CSS selector for supplemental text"""
    dir="comics"
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
    encoding="utf-8"
    """
    Text encoding of the comic site.

    In the future this will be auto-detected
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

    def __init__(self, url:str=None, number:int=1, floating:bool=True):
        """Creates a Comic object, downloads and parses the comic page"""
        self.url=self.match(url)
        self.floating = floating and (self.url!=self.first) #if the URL points to the first comic, it's not "floating"
        self.number=number

    def setDir(self, dir):
        self.dir=dir

    def load(self):
        """Downloads the webpage. Pretty important for most of the stuff in this class"""
        if(self.dom is None):
            print("Downloading webpage {0}".format(self.url))
            response=requests.get(self.url, headers=self.headers)
            #TODO: try to get encoding from response header
            self.dom=html.fromstring(response.text)
            #TODO: try to get encoding from meta tags

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
            return e.attrib[attr].strip()
        else:
            return ""

    def _getText(self, selector:str, dom=None):
        """Return the text of the first element matching the given selector"""
        e=self._getElement(selector, dom)
        if(e is not None):
            return e.text.strip()
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

    def getSupplementalText(self):
        if(self.textSelector):
            text=etree.tostring(self._getElement(self.textSelector), method="text", encoding="utf-8")
            text=text.strip().decode(self.encoding)
            text=re.sub('\s+', ' ', text)
            if(text):
                return text or None
        else:
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
        url=self.getNextURL()
        return (url is not None) and (url.rstrip("/#") != self.url.rstrip("/#"))

    def getNextComic(self, url:str=None):
        """Return a Comic object corresponding to the next comic"""
        if(url or self.hasNext()):
            comic=self.__class__(
                    url      = url or self.getNextURL(),
                    number   = None if self.number is None else self.number+1,
                    floating = self.floating)
            comic.setDir(self.dir)
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
        return d

    def download(self, dirname:str=None, overwrite=False):
        """Download the image, saving it in the specified directory. Saves under a different name and then moves it, to improve integrity"""
        if(not os.path.isdir(self.dir)):
            os.mkdir(self.dir)
        if(self.getImg()):
            self.downloadImage(
                    os.path.join(self.dir, self.getImgFilename()),
                    self.getImg(),
                    overwrite
                    )
        if(self.getBonusImg()):
            self.downloadImage(
                    os.path.join(self.dir, self.getBonusImgFilename()),
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
