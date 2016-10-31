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
