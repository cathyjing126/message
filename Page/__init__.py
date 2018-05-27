from selenium.webdriver.common.by import By
# 新增短信按钮
sms_add_btn=(By.ID,'com.android.mms:id/action_compose_new')
#添加手机号码文本框
phone_add_text=(By.ID,'com.android.mms:id/recipients_editor')
#短信输入文本框
mass_input_text=(By.ID,'com.android.mms:id/embedded_text_editor')
#发送短信按钮
mass_send_btn=(By.ID,'com.android.mms:id/send_button_sms')
# 获取已发送内容
mass_get_send_text = (By.ID, "com.android.mms:id/text_view")


# 搜索按钮
search_btn = (By.ID, "com.android.settings:id/search")
# 输入框
search_input = (By.ID, "android:id/search_src_text")
# 结果列表
search_result = (By.ID, "com.android.settings:id/title")

# 菜单按钮
menu_btn = (By.CLASS_NAME, "android.widget.ImageButton")

#退出账户按钮
account_btn = (By.XPATH, "退出登录")