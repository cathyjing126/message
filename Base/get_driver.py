from appium import webdriver
def get_driver_sc():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "sx",
        "appPackage": "com.android.settings",  # 设置包名
        "appActivity": ".Settings", # 设置启动名
        "unicodeKeyboard" :True,
        "resetKeyboard":True
    }
    return  webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
def get_driver_mes():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "sx",
        "appPackage": "com.android.mms",  # 短信包名
        "appActivity": ".ui.ConversationList",  # 短信启动名
        "unicodeKeyboard" :True,
        "resetKeyboard":True
    }
    return  webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
def get_driver_dairy():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "sx",
        "appPackage": "com.chenupt.day",  # 一本日记包名
        "appActivity": ".MainActivity",  # 一本日记启动名
        "unicodeKeyboard" :True,
        "resetKeyboard":True
    }
    return  webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
