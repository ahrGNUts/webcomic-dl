from webcomic_dl.comics import *
def getComic(url: str):
    """Return a new Comic object for the given url"""
    for c in vars()["Comics"].__subclasses__():
        if c.match(url):
            return c(url)
    return Comic(url)

class Comic:
    #the CSS selector for the "next" link
    nextSelector=""
    #the CSS selector for the comic title
    titleSelector=""
    #the CSS selector for the comic img
    imgSelector=""
    #the CSS selector for supplemental text
    textSelector=""
    #the title of the site
    siteTitle=""
    #the default directory name to download into
    defaultDirname=""
    #the regex for matching the URL to the Comic
    urlRegex=".*"
    @classmethod
    def match(cls, url:str):
        """Returns whether this Comic class will work for the given URL"""
        return re.match(cls.urlRegex, url)

    def __init__(self, url:str):
        """Creates a Comic object, downloads and parses the comic page"""
        self.url=url
        self.dom=None

    def _getText(self, selector:str):
        """Return the text of the first element matching the given selector"""

    def _getAttr(self, selector:str, attr:str):
        """Return the value of the given attribute for the first element matching the given selector"""

    def getNumber(self):
        """Return the page number"""
        return 0

    def getTitle(self):
        """Return the title of this comic"""
        return self.getHref(self.titleSelector)

    def getImg(self):
        """Return the image URL for this page"""
        return self._getAttr(self.imgSelector, "src")

    def getImgExtension(self):
        """Return the filename extension for the image"""
        return re.match(r'\.([a-zA-Z]+$', self.getImg()).group(1)

    def getImgFile(self):
        """Return the filename to save the image as"""
        return "{number:06d} {title:s}.{extension:s}".format(number=self.getNumber(), title=self.getTitle(), extension=self.getExtension())

    def getAlt(self):
        """Return the alt text for this comic"""
        return self._getAttr(self.imgSelector, "alt")

    def getText(self):
        """Return any accompanying text for this comic"""
        return  self._getText(self.textSelector)

    def getNext(self):
        """Return the URL of the next page if there is one, or False otherwise"""
        return self.getHref(nextSelector)

    def toDict(self):
        """Returns a dict with all the important stuff"""
        return {
                "number": self.getNumber(),
                "title": self.getTitle(),
                "url": self.url,
                "imgurl": self.getImg(),
                "imgfile": self.getImgFile(),
                "alt": self.getAlt(),
                "text": self.getText()
                }
