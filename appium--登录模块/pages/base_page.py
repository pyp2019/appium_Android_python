from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_ini import ReadIni


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # 读取配置文件
    def get_local_config(self, local_config, node=None, file_name=None):
        read_ini = ReadIni(node=node, file_name=file_name)
        info = read_ini.get_value_tuple(local_config)
        return info

    def get_element(self, local_config, node=None, file_name=None, element=None):
        """
        获取寻常的element
        :param local_config: 配置信息key
        :param node: 配置信息头[]
        :param file_name: 配置文件路径
        :param element: 元素定位要素
        :return:
        """
        ini = self.get_local_config(local_config, node, file_name)
        if ini is None:
            return None
        locator = (ini[0], ini[1])
        try:
            if element:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of(element.find_element(*locator)))
            else:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=locator))
        except TimeoutException:
            # self.driver.quit()
            raise TimeoutException(msg="定位元素失败，定位方式是:{}".format(locator))
        except NoSuchElementException:
            # self.driver.quit()
            raise NoSuchElementException(msg="定位元素失败，定位方式是:{}".format(locator))


# if __name__ == "__main__":
#     base = BasePage()
#     info = base.get_local_config("username", None, None)
#     print(info)
