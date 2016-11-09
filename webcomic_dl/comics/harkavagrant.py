from webcomic_dl import Comic
from webcomic_dl.webpage import Webpage
import re
class HarkAVagrantComic(Comic):
    nextSelector='table td[colspan="2"] > center:first-child a:nth-child(3)'
    imgSelector='table td[colspan="2"] > center > .rss-content > img'
    siteTitle="Hark! A Vagrant"
    directory="Hark! A Vagrant"
    urlRegex='^https?://(?:www\.)?harkavagrant\.com(?:/|$)'
    name="harkavagrant"
    first="http://www.harkavagrant.com/index.php?id=1"
    textSelector=".black11 .rss-content"
    printSelector='table td[colspan="2"] > center:last-child a:last-child'

    def getTitle(self):
        return self.getAlt()

    def getNumber(self):
        return int(re.search(r'\d+$', self.url).group(0))
