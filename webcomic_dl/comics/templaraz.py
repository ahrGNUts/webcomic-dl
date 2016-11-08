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
    firstSelector=".nav-first > a"
    
    def getNumber(self):
        self.load()
        if(self.page.getElement(self.firstSelector) is None):
            return 1;
        else:
            super().getNumber()
