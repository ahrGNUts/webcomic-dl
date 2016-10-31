from webcomic_dl import Comic
import re
class SmbcComic(Comic):
    nextSelector="a.next"
    titleSelector="title"
    imgSelector="#cc-comic"
    siteTitle="Saturday Morning Breakfast Cereal"
    defaultDirname="SMBC"
    urlRegex="^https?://(?:www\.)?smbc-comics\.com(?:/|$)"
    name="smbc"
    first="http://www.smbc-comics.com/comic/2002-09-05"

    def getTitle(self):
        return self._getText("title")
        return re.search(r'^Saturday Morning Breakfast Cereal - (.*)$', self._getText("title")).groups(1)[0]

    def getNumber(self):
        if(self.floating):
            print("downloading index")
            dom=self.getDOM("http://smbc-comics.com/comic/archive")
            elements=self._getElements("select[name='comic'] > option", dom)
            for i, e in enumerate(elements):
                if(self.url.rstrip("/").endswith("/" + e.attrib["value"])):
                    self.number=i
                    self.floating=False
                    break
        return self.number
