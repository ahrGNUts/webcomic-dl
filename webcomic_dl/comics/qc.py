from webcomic_dl import Comic
import re
class QuestionableContentComic(Comic):
    nextSelector="#comicnav li:nth-child(3) a"
    titleSelector=False
    imgSelector="#strip"
    siteTitle="Questionable Content"
    dir="Questionable Content"
    urlRegex="^https?://(?:www\.)?questionablecontent\.net(?:/|$)"
    name="questionable-content"
    first="https://questionablecontent.net/view.php?comic=1"
    textSelector="#news"
    def getNumber(self):
        return int(re.search(r'comic=(\d+)', self.url).group(1))
