from webcomic_dl import Comic
from webcomic_dl.webpage import Webpage
import re
class SmbcComic(Comic):
    nextSelector="a.next"
    titleSelector="title"
    imgSelector="#cc-comic"
    bonusSelector="#aftercomic > img"
    siteTitle="Saturday Morning Breakfast Cereal"
    directory="SMBC"
    urlRegex="^https?://(?:www\.)?smbc-comics\.com(?:/|$)"
    name="smbc"
    first="http://www.smbc-comics.com/comic/2002-09-05"

    def getTitle(self):
        return re.search(r'^Saturday Morning Breakfast Cereal - (.*)$', self.page.getText("title")).groups(1)[0]

    def getNumber(self):
        if(self.number is None):
            print("downloading index")
            page=Webpage("http://smbc-comics.com/comic/archive")
            elements=page.getElements("select[name='comic'] > option")
            for i, e in enumerate(elements):
                if(self.url.rstrip("/").endswith("/" + e.attrib["value"])):
                    self.number=i
                    break
        return self.number
