"""
    页面层/元素层
            /注册页面元素定位
"""

from pages.base_page import BasePage


class RegisterPage():
    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(self.driver)

    def get_login_element(self):
        """获取跳转登陆页面的element"""
        return self.base.get_element("login_button", node="register_element")


# if __name__ == "__main__":
#     ll = RegisterPage(driver)
#     ll.get_login_element()