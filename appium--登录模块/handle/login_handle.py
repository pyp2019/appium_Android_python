"""
    操作层
        /登录页面元素的操作
"""
from pages.login_page import LoginPage


class LoginHandle():
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def send_username(self, username):
        """在用户名输入栏输入username"""
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        """在密码输入栏输入password"""
        self.login_page.get_password_element().send_keys(password)

    def click_login_button(self):
        """点击登录按钮"""
        self.login_page.get_login_button_element().click()

    def click_forgot_password_button(self):
        """点击忘记密码按钮"""
        self.login_page.get_forget_password_button_element().click()

    def click_register_button(self):
        """点击注册按钮"""
        self.login_page.get_register_button_element().click()

    def get_fail_tost(self, message):
        """判断是否有tost"""
        try:
            return message == self.login_page.get_tost_element(message).text
        except:
            return False