import re
class Site:
    regex='https?://.*\..*'
    def match(url:string):
        """Returns whether this Site class will work for the given url"""

    first=""
    def __init__(self, url:strig=None):
        """Creates a Site object"""
        self.url=url if url else self.first
        self.dom=None
    
    comicClass=""
    def getComic(self):
        """Return the current Comic object. Each call advances to the next comic."""

    title=""

    dirname=""

    def getComics(self, max:int=None):
        """Return a list of all the comics, up to a maximum of max"""
