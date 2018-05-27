import sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/..')
from Page.Page import Page
from Base.get_driver import get_driver_sc
from Base.Read_Data import Read_Data
import pytest

def read_search_data():
    da_list = []
    data = Read_Data("search_data").get_test_data()

    for i in data.get("search_data"):
        da_list.append((i.get("data").get("input"), i.get("data").get("expect")))

    return da_list

class Test_Search:
    def setup_class(self):
        self.page_obj = Page(get_driver_sc())
        # 点击搜索按钮
        self.page_obj.get_search_page().click_search()
    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("input,expect",read_search_data())
    def test_search_text(self,input,expect):
        # print("input:%s\nexpect:%s",(input,expect))
        # 搜索输入内容
        result = self.page_obj.get_search_page().search_text(input)

        assert expect in result
if __name__ == '__main__':
    pytest.main('-s test_search1.py')


