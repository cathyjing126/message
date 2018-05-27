import sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/..')
from Page.Page import Page
from Base.get_driver import get_driver_mes
from Base.Read_Data import Read_Data
import pytest
import yaml
def mess_data():
    da_list=[]
    with open ('../Data/mess_data.yml','r',encoding='utf-8') as f:
        data1 = yaml.load(f)
        for i in data1.get('sms_data').values():
            da_list.append(i)
    return da_list
# def read_search_data():
#     da_list = []
#     data = Read_Data("mess_data").get_test_data1()
#     for i in data.get("mess_data"):
#         da_list.append(i)

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
    @pytest.mark.parametrize("send_text",mess_data())
    def test_mess_send(self,send_text):
        #发送短信
        send_result=self.page_obj.get_mess_page().send_sms(send_text)
        assert send_text in send_result
if __name__ == '__main__':
    pytest.main('-s test_mess.py')