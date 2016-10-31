from webcomic_dl import Comic
import re
class DinosaurComic(Comic):
    nextSelector='a[title="Next comic"]'
    titleSelector=False
    imgSelector="img.comic"
    siteTitle="Dinosaur Comics"
    defaultDirname="Dinosaur Comics"
    urlRegex="^https?://(?:www\.)?qwantz\.com(?:/|$)"
    name="dinosaur-comics"
    first="http://www.qwantz.com/index.php?comic=1"
    def getNumber(self):
        return int(re.search(r'comic=(\d+)', self.url).group(1))
