import time
from utils.read_ini import ReadIni
from appium import webdriver

from utils.server import Server


class BaseDriver():
    def android_driver(self, i):
        ini = ReadIni(node="server_port", file_name=r"D:\测试\自动化测试\App自动化测试\appium--慕课网登录模块\config\userconfig.ini")
        deviceName = ini.get_value("devices" + str(i))
        port = ini.get_value("appium_port" + str(i))
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": deviceName,
            "app": "D:\\测试\\APPnium\\mukewang.apk",
            "noReset": "true"
        }
        driver = webdriver.Remote("127.0.0.1:" + port +"/wd/hub", capabilities)
        time.sleep(5)
        return driver


if __name__ == "__main__":
        base_driver = BaseDriver()
        base_driver.android_driver()