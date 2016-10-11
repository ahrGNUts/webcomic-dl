class XkcdComic(Comic):
    nextSelector="a[rel=next]"
    titleSelector="#ctitle"
    imgSelector="#comic img"
    textSelector=False
    siteTitle="xkcd"
    defaultDirname="xkcd"
    urlRegex="^https?://xkcd\.com(?:/|$)"
    def getNumber(self):
        return re.match(r'\d+', self.url).group(0)
