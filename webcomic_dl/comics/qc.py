from webcomic_dl import Comic
import re
class QuestionableContentComic(Comic):
    nextSelector="#comicnav li:nth-child(3) a"
    titleSelector=False
    imgSelector="#strip"
    siteTitle="Questionable Content"
    defaultDirname="Questionable Content"
    urlRegex="^https?://(?:www\.)?questionablecontent\.net(?:/|$)"
    def getNumber(self):
        return int(re.search(r'comic=(\d+)', self.url).group(1))
