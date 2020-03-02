from handle.login_handle import LoginHandle


class LoginBusiness():
    def __init__(self, driver):
        self.login_handle = LoginHandle(driver)

    def base_login(self, username, password):
        """
        登陆操作
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.login_handle.send_username(username)
        self.login_handle.send_password(password)
        self.login_handle.click_login_button()

    def error_login(self, assertText):
        """ 当没有tost的同时，也没有登录按钮就算登陆成功了 """
        if self.login_handle.get_fail_tost(assertText):
            return True
        else:
            try:
                self.login_handle.click_login_button()
            except:
                return False
            else:
                return True

    def pass_login(self, assertText):
        """ 当没有tost的同时，也没有登录按钮就算登陆成功了 """
        if self.login_handle.get_fail_tost(assertText):
            return False
        else:
            try:
                self.login_handle.click_login_button()
            except:
                return True
            else:
                return False

    def login_pass(self, username, password):
        """
        登录成功case
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.base_login(username, password)
        try:
            self.login_handle.send_password("a")
            return False
        except:
            return True

    def username_error(self, username, password):
        """
        账号失败case
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.base_login(username, password)
        return self.error_login("请输入密码")

    def password_error(self, username, password):
        """
        密码失败case
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.base_login(username, password)
        return self.error_login("请输入密码")

    def login_case(self, username, password, assertCode, assertText):
        """
        登录模块case处理
        :param username: 账号
        :param password: 密码
        :param assertCode: 错误类型
        :param assertText: 错误提示
        :return: case执行结果
        """
        try:
            self.base_login(username, password)
        except:
            return False
        if "error" in assertCode:
            return self.error_login(assertText)
        else:
            return self.pass_login(assertText)

