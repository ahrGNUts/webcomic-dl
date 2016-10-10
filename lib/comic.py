import comics.*
class getComic(url:string):
    """Return a new Comic object for the given url"""
    for c in vars()["Comics"].__subclasses__():
        if(c.match(url)):
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
    def match(cls, url:string):
        """Returns whether this Comic class will work for the given URL"""
        return re.match(cls.urlRegex, url)
    
    def __init__(self, url:string):
        """Creates a Comic object, downloads and parses the comic page"""
        self.url=url
        self.dom=None

    def getText(self, selector:string):
        """Return the text of the first element matching the given selector"""

    def getAttr(self, selector:string, attr:string):
        """Return the value of the given attribute for the first element matching the given selector"""

    def getNext(self):
        """Return the URL of the next page if there is one, or False otherwise"""
        return self.getHref(nextSelector)

    def getNumber(self):
        """Return the page number"""
        return 0

    def getTitle(self):
        """Return the title of this comic"""
        return self.getHref(self.titleSelector)

    def getImg(self):
        """Return the image URL for this page"""
        return self.getAttr(self.imgSelector, "src")

    def getAlt(self):
        """Return the alt text for this comic"""
        return self.getAttr(self.imgSelector, "alt")

    def getAccompanyingText(self):
        """Return any accompanying text for this comic"""
        return  getText(self.textSelector)
