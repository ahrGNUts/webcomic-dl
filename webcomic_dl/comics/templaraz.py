from webcomic_dl import Comic
from webcomic_dl.webpage import Webpage
import re
class TemplarAZComic(Comic):
    nextSelector="a[rel=next]"
    imgSelector="#comic > img"
    siteTitle="Templar, Arizona"
    directory="Templar, Arizona"
    urlRegex=r'^((?:.+[/\.])?templaraz\.com)(/|$)'
    name="templaraz"
    first="http://templaraz.com/2005/05/26/chapter-1-the-great-outdoors-cover/"
    firstSelector=".nav-first > a"
    
    def getNumber(self):
        self.load()
        if(self.page.getElement(self.firstSelector) is None):
            return 1;
        else:
            super().getNumber()
