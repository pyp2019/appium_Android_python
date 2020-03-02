import HTMLTestRunner
import datetime
import os
import time
import unittest
import ddt
from Business.login_business import LoginBusiness
from utils.base_driver import BaseDriver
from utils.excel_util import ExcelUtil
from utils.send_report import send_mail
from utils.server import Server


ex = ExcelUtil()
data = ex.get_data()


@ddt.ddt
class LoginCaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_driver = BaseDriver()
        cls.driver = base_driver.android_driver(0)
        time.sleep(10)
        cls.login_business = LoginBusiness(cls.driver)

    @ddt.data(*data)
    def test_login_case(self, data):
        username, password, assertCode, assertText = data
        login_case = self.login_business.login_case(username, password, assertCode, assertText)
        self.assertTrue(login_case, "case执行失败")


if __name__ == "__main__":
    se = Server()
    se.start_server_thread()
    now = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/report/" + now + "_case.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCaseTest)
    with open(file_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f)
        runner.run(suite)

    # 发送报告到邮箱
    send_mail("1134636122@qq.com", "TestResult", file_path)