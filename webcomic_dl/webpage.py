import requests
import re
from lxml import html, etree
from lxml.cssselect import CSSSelector
from urllib.parse import urljoin
import os.path
import os
import json

class Webpage:
    url=""
    """URL of the webpage"""
    dom=None
    """The page's DOM"""
    encoding=None
    """The page's encoding"""

    def __init__(self, url:str, headers:dict=None, encoding:str=None):
        self.url=url
        response=requests.get(url)
        if(encoding):
            self.encoding=encoding
        else:
            self.encoding=self.parseContentType(response.headers.get("Content-Type", ""))
        if(self.encoding is None):
            self.encoding="utf-8"
        self.dom=html.fromstring(response.text)

    @staticmethod
    def parseContentType(string):
        result=re.search(r'charset=[^;]+', string)
        if(result and len(result.groups()) > 1):
            return result.group(1)
        return None

    def getElements(self, selector:str):
        """Return all elements matching the given selector"""
        if not selector:
            return None
        sel=CSSSelector(selector)
        e=sel(self.dom)
        return e

    def getElement(self, selector:str):
        """Return the first element matching the given selector"""
        e=self.getElements(selector)
        if(e is not None and len(e)):
            return e[0]
        return None

    def getAttr(self, selector:str, attr:str):
        """Return the value of the given attribute for the first element matching the given selector"""
        e=self.getElement(selector)
        if(e is not None and attr in e.attrib):
            return e.attrib[attr].strip()
        else:
            return ""

    def getURL(self, selector:str, attr:str="href"):
        """
        Return the value of 'attr' for the first element matching 'selector', treating it like a URL and resolving relative URLs to the page URL.
        """
        src=self.getAttr(selector, attr)
        if(src):
            return urljoin(
                    self.url,
                    src
                    )
        return None

    def getText(self, selector:str):
        """Return the text of the first element matching the given selector, with some aggressive whitespace stripping"""
        if(selector):
            element=self.getElement(selector)
            if(element is not None):
                text=etree.tostring(element, method="text", encoding=self.encoding)
                #strip all leading and trailing whitespace
                text=text.decode(self.encoding).strip()
                #if a sequence of whitespace chars has a newline in it, replace with a single newline
                text=re.sub(r'\s*\n\s*', '\n', text)
                #replace any remaining whitespace sequences with a single space
                text=re.sub('\s{2,}', ' ', text)
                if(text):
                    return text
        return None
