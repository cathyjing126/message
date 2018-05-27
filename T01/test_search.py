import sys,os
sys.path.append(os.getcwd())
from Page.Page import Page
from Base.get_driver import get_driver_sc
import pytest

class Test_Search:
    def setup_class(self):
        #实例化page页面对象
        self.page_obj=Page(get_driver_sc())
        # 点击搜索按钮
        self.page_obj.get_search_page().click_search()
    def teardown_class(self):
        #关闭页面驱动对象
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("text_value,expect",[(1,"休眠"),("ip","IP地址"),("mtp","媒体设备(MTP)")])#
    def test_search_input(self,text_value,expect):
        # 输入搜索内容,获取搜索结果列表
        result=self.page_obj.get_search_page().search_text(text_value)
        # 断言结果
        assert expect in result

if __name__ == '__main__':
    pytest.main('-s test_search.py')

