class Comic:
    def __init__(self, url:string):
        """Creates a Comic object, downloads and parses the comic page"""
        self.url=url
        self.dom=None
    
    def getText(self, selector:string):
        """Return the text of the first element matching the given selector"""

    def getAttr(self, selector:string, attr:string):
        """Return the value of the given attribute for the first element matching the given selector"""

    nextSelector=""
    def getNext(self):
        """Return the URL of the next page if there is one, or False otherwise"""
        return self.getHref(nextSelector)

    def getNumber(self):
        """Return the page number"""
        return 0

    titleSelector=""
    def getTitle(self):
        """Return the title of this comic"""
        return self.getHref(self.titleSelector)

    imgSelector=""
    def getImg(self):
        """Return the image URL for this page"""
        return self.getAttr(self.imgSelector, "src")

    def getAlt(self):
        """Return the alt text for this comic"""
        return self.getAttr(self.imgSelector, "alt")

    textSelector=""
    def getAccompanyingText(self):
        """Return any accompanying text for this comic"""
        return  getText(self.textSelector)
