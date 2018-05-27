import sys,os
sys.path.append(os.getcwd())
from Page.Page import Page
from Base.get_driver import get_driver_mes
import pytest
class Test_Mess:
    def setup_class(self):
        self.page_obj=Page(get_driver_mes())
    def teardown_class(self):
        self.page_obj.driver.quit()
    @pytest.fixture(scope='class',autouse=True)
    def add_phonenum(self):
        #点击新建短信
        self.page_obj.get_mess_page().add_sms()
        #输入手机号
        self.page_obj.get_mess_page().add_phone('1871788888')
    @pytest.mark.parametrize("send_ms",["hello","你好","bye"])
    def test_mess_send(self,send_ms):
        #发送短信
        send_result=self.page_obj.get_mess_page().send_sms(send_ms)
        assert send_ms in send_result
if __name__ == '__main__':
    pytest.main('-s test_mess.py')