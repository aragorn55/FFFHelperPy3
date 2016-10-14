from fanficfare.geturls import get_urls_from_text
from fanficfare import adapters
from chrome_bookmark_reader import ChromeBookmarkParser

class FanFicFareHelper(object):

    def get_fanficfare_urls(self, url_list):
        for url_item in url_list:
            self.getNormalStoryURL(url_item)


    def getNormalStoryURL(self, url):
        r = adapters.getNormalStoryURLSite(url)
        if r:
            print('Url: ' + r[0])
            print('Site: ' + r[1])
        else:
            print('no reaturn: ' + url)

    def get_urls_from_chrome_bookmark(self, sPath):
        reader = ChromeBookmarkParser()
        url_list = reader.simple_get_urls(sPath)
        return url_list
