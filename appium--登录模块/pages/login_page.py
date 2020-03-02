"""
    页面层/元素层
            /登陆页面元素定位
"""
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def get_username_element(self):
        """获取username输入栏的element"""
        return self.base.get_element("username")

    def get_password_element(self):
        """获取password输入栏的element"""
        return self.base.get_element("password")

    def get_login_button_element(self):
        """获取login_button按钮的element"""
        return self.base.get_element("login_button")

    def get_forget_password_button_element(self):
        """获取忘记密码按钮的element"""
        return self.base.get_element("forget_password_button")

    def get_register_button_element(self):
        """获取注册的按钮的element"""
        return self.base.get_element("register_button")

    def get_tost_element(self, message):
        """获取tost的element"""
        time.sleep(2)
        # 获取test的定位控件
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))