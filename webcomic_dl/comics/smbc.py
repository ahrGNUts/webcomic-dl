import webcomic_dl
import re
class SmbcComic(webcomic_dl.Comic):
    nextSelector="a.next"
    titleSelector="title"
    imgSelector="#cc-comic"
    siteTitle="Saturday Morning Breakfast Cereal"
    defaultDirname="SMBC"
    urlRegex="^https?://(?:www\.)?smbc-comics\.com(?:/|$)"

    def getTitle(self):
        return re.search(r'^Saturday Morning Breakfast Cereal - (.*)$', self._getText("title")).groups(1)[0]

    def getNumber(self):
        return 1
