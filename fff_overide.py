from past import autotranslate
autotranslate(['fanficfare.adapters'])
autotranslate(['fanficfare.configurable'])
import fanficfare.adapters
from fanficfare import adapters
from fanficfare.configurable import Configuration

class FFFOverides(object):
    def getNormalStoryURLSite(url):
        # print("getNormalStoryURLSite:%s"%url)
        if not adapters.gerNormalStoryURL.__dummyconfig:
            adapters.getNormalStoryURL.__dummyconfig = Configuration(["test1.com"], "EPUB", lightweight=True)
        # pulling up an adapter is pretty low over-head.  If
        # it fails, it's a bad url.
        try:
            adapter = adapters.getAdapter(adapters.getNormalStoryURL.__dummyconfig, url)
            url = adapter.url
            site = adapter.getSiteDomain()
            storyid = adapter.story.getMetadata('storyId')
            del adapter
            return (url, site, storyid)
        except:
            return None