from Base.Base import Base
import Page
class Mess_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击短信添加按钮
    def add_sms(self):
        self.click_element(Page.sms_add_btn)
    # 输入手机号
    def add_phone(self,phone):
        self.input_element(Page.phone_add_text,phone)

    def send_sms(self,send_text):
        # 输入短信内容
        self.input_element(Page.mass_input_text,send_text)
        #点击发送按钮
        self.click_element(Page.mass_send_btn)
        #获取结果列表
        result_sms=self.search_elements(Page.mass_get_send_text,timeout=5)
        return [i.text for i in result_sms]
