from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
class Base:
    def __init__(self,driver):
        self.driver=driver
    #定位单个元素
    def search_element(self,loc,to=10):
        return WebDriverWait(self.driver,timeout=to).until(lambda x : x.find_element(*loc))
    #定位一组元素
    def search_elements(self,loc,to=10):
        return WebDriverWait(self.driver,timeout=to).until(lambda x : x.find_elements(*loc))
    #点击元素
    def click_element(self,loc):
        self.search_element(loc).click()
    #输入内容
    def input_element(self,loc,text):
        self.search_element(loc).send_keys(text)