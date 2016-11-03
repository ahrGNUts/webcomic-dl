from webcomic_dl import Comic
import re
class XkcdComic(Comic):
    nextSelector="a[rel=next]"
    titleSelector="#ctitle"
    imgSelector="#comic img"
    siteTitle="xkcd"
    directory="xkcd"
    urlRegex="^https?://xkcd\.com(?:/|$)"
    name="xkcd"
    first="https://xkcd.com/1"
    def getNumber(self):
        return int(re.search(r'\d+', self.url).group(0))
