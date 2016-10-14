#from fanficfare_helper import FanFicFareHelper
from futurize import ProcessFiles
#path = r"C:\Users\joshua\AppData\Local\Google\Chrome\User Data\Profile 1\Bookmarks"
path = r"C:\G\IDE\pycharm\FFFHelperPy3\fanficfare"
proc = ProcessFiles()
file_list = proc.walker(path)
for item in file_list:
    proc.future(item)
#helper = FanFicFareHelper()
#urls = helper.get_urls_from_chrome_bookmark(path)
#helper.get_fanficfare_urls(urls)
#helper.write_links()
# from addventure import Episode
# from addventure import Choice
# from create_be_db import AddventureDB
# from bearchive_process import BEarchive_process
# from be_sql_builder import BeSql

print('done')