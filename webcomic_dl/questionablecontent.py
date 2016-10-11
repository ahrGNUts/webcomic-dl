class QuestionableContentComic(Comic):
    nextSelector="#comicnav li:nth-child(3) a"
    titleSelector=False
    imgSelector="#strip"
    textSelector="#news"
    siteTitle="Questionable Content"
    defaultDirname="Questionable Content"
    urlRegex="^https?://(?:www\.)?questionablecontent\.net(?:/|$)"
    def getNumber(self):
        return re.match(r'comic=(\d+)', self.url).group(1)
