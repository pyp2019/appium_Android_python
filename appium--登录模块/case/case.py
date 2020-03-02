import HTMLTestRunner
import os
import time
import unittest

from utils.send_report import send_mail


class LoginCaseTest(unittest.TestCase):

    def setUp(self):
        self.initdata = "hello imooc"

    def test_something(self):
        self.assertEqual("hello imooc", self.initdata)

    def tearDown(self):
        pass


if __name__ == "__main__":
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/report/" + "login_case.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCaseTest)
    with open(file_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f)
        runner.run(suite)

    send_mail("1134636122@qq.com", "TestResult", file_path)