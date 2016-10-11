import webcomic_dl
import re
class XkcdComic(webcomic_dl.Comic):
    nextSelector="a[rel=next]"
    titleSelector="#ctitle"
    imgSelector="#comic img"
    siteTitle="xkcd"
    defaultDirname="xkcd"
    urlRegex="^https?://xkcd\.com(?:/|$)"
    def getNumber(self):
        return int(re.search(r'\d+', self.url).group(0))
