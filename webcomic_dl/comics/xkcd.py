from webcomic_dl import Comic
import re
class XkcdComic(Comic):
    nextSelector="a[rel=next]"
    titleSelector="#ctitle"
    imgSelector="#comic img"
    siteTitle="xkcd"
    defaultDirname="xkcd"
    urlRegex="^https?://xkcd\.com(?:/|$)"
    def getNumber(self):
        return int(re.search(r'\d+', self.url).group(0))
