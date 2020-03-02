import configparser


class ReadIni():
    def __init__(self, node=None, file_name=None):
        if file_name is None:
            self.file_name = r"D:\测试\自动化测试\App自动化测试\appium--慕课网登录模块\config\LocalElement.ini"
        else:
            self.file_name= file_name
        if node is None:
            self.node = "login_element"
        else:
            self.node = node
        self.data = self.load_ini(self.file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8-sig")
        return cf

    def write_ini(self, selection, option, value):
        try:
            self.data.add_section(selection)  # 设置option的值
        except:
            pass
        self.data.set(selection, option, value)  # 注意这里的selection一定要先存在！
        self.data.set(selection, option, value)
        with open(self.file_name, 'w') as configfile:
            self.data.write(configfile)

    # 获取key的value
    def get_value(self, key):
        try:
            return self.data.get(self.node, key)
        except:
            return None

    # 拆分>字符两端的字符串并返回list
    def get_value_tuple(self, key):
        data = self.get_value(key)
        if data is None:
            return None
        data_info = data.split(">")
        return data_info


# if __name__ == "__main__":
#     ini = ReadIni(node="server_port", file_name=r"D:\测试\自动化测试\App自动化测试\Appnium\config\userconfig.ini")
#     a = ini.get_value("appium_port0")
#     print(a)
