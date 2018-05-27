from Base.Base import Base
import Page
class Dairy_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击菜单按钮
    def click_menu(self):
        result=self.click_element(Page.menu_btn).text


