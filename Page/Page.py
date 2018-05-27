from Page.search_page import Search_Page
from Page.mess_page import Mess_Page
from Page.dairy_page import Dairy_Page
class Page:
    def __init__(self,driver):
        self.driver=driver
    #搜索页面
    def get_search_page(self):
        return Search_Page(self.driver)
    #信息页面
    def get_mess_page(self):
        return Mess_Page(self.driver)
    #日记页面
    def get_dairy_page(self,driver):
        return Dairy_Page(driver)

