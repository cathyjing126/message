from Base.Base import Base
import Page
class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击搜索按钮
    def click_search(self):
        self.click_element(Page.search_btn)
    # 输入内容并搜索
    def search_text(self,text_value):
        self.input_element(Page.search_input,text_value)
        #获取结果列表
        result= self.search_elements(Page.search_result)
        return [i.text for i in result]