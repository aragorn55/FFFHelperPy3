#from fanficfare.geturls import get_urls_from_text
#from past import autotranslate
#autotranslate(['fanficfare'])
#from fanficfare import adapters
from chrome_bookmark_reader import ChromeBookmarkParser
from fff_overide import FFFOverides
from fanficfare.configurable import Configuration
#from fanficfare.story import Story
class FanFicFareHelper(object):
    _fff_story_list = []
    _misc_list = []
    _fff_overide = FFFOverides()

    def get_fanficfare_urls(self, url_list):
        for url_item in url_list:
#            self._fff_overide.getNormalStoryURLSite(url_item)
            self.getNormalStoryURL_test(url_item)
           # self.convert_fic(url_item)

    def write_links(self):
        file = open("fff_links.csv", "w")
        for item in self._fff_story_list:
            file.write(item)
        file.close()
        misc = open("misc.csv", "w")
        for value in self._misc_list:
            misc.write(value)
        misc.close()

    def getNormalStoryURL_test(self, url):
        r = self._fff_overide.getNormalStoryURLSite(url)
#        r = adapters.getNormalStoryURLSite(url)
        if r:
            record = r[0]+ ";" + r[1] + ";" + r[2] +"\n"
            self._fff_story_list.append(record)

#            print('Url: ' + r[0])
#            print('Site: ' + r[1])
#            print('FicId: ' + r[2])
        else:
            self._misc_list.append(url + "\n")
#            print('no reaturn: ' + url)

    def convert_fic(self, url):
        print_fic = self.getNormalStoryURLSite_test(url)
        if print_fic:
            print('Url: ' + print_fic.FicUrl)
            print('Site: ' + print_fic.ArchiveDomain)
            print('FicId: ' + print_fic.ArchiveID)
        else:
            print('no reaturn: ' + url)


    def get_urls_from_chrome_bookmark(self, sPath):
        reader = ChromeBookmarkParser()
        url_list = reader.simple_get_urls(sPath)
        return url_list




class FanFicFareData(object):
    _FicURL = ''
    _FanFicFareID = ''
    _ArchiveID = ''
    _ArchiveDomain = ''
    @property
    def FicUrl(self):
        return self._FicUrl

    @FicUrl.setter
    def FicUrl(self, value):
        self._FicUrl = value

    @property
    def ArchiveDomain(self):
        return self._ArchiveDomain

    @ArchiveDomain.setter
    def ArchiveDomain(self, value):
        self._ArchiveDomain = value

    @property
    def ArchiveID(self):
        return self._ArchiveID

    @ArchiveID.setter
    def ArchiveID(self, value):
        self._ArchiveID = value

    @property
    def FanFicFareID(self):
        return self._FanFicFareID

    @FanFicFareID.setter
    def FanFicFareID(self, value):
        self._FanFicFareID = value