"""
    处理cmd命令执行结果，使之符合所需信息的格式
"""
import time

from utils.dos_cmd import DosCmd
from utils.port import Port
import threading
from utils.read_ini import ReadIni


class Server(object):
    def __init__(self):
        self.dos = DosCmd()
        self.ini = ReadIni(file_name=r"D:\测试\自动化测试\App自动化测试\appium--慕课网登录模块\config\userconfig.ini")

    def kill_node_server(self):
        server_list = self.dos.execute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.execute_cmd("taskkill -F -PID node.exe")

    def get_devices(self):
        """
        获取设备信息
        :return: 格式化后的设备信息
        """
        devices = self.dos.execute_cmd_result("adb devices")
        if len(devices) >= 2:
            result = [i.replace("\tdevice", "") for i in devices if "\tdevice" in i]
        else:
            result = None
        return result

    def connect_device(self, devices_list):
        for i in devices_list:
            self.dos.execute_cmd("adb connect " + i)

    def create_port_list(self, start_port):
        """获取port"""
        p = Port()
        port_list = p.create_port_list(start_port, self.get_devices())
        return port_list

    def create_command_list(self):
        """创建一个启动appium的cmd命令"""
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        devices_list = self.get_devices()
        self.connect_device(devices_list)
        for i in range(len(devices_list)):
            self.ini.write_ini("server_port", "appium_port" + str(i), str(appium_port_list[i]))
            self.ini.write_ini("server_port", "bootstrap_port" + str(i), str(bootstrap_port_list[i]))
            self.ini.write_ini("server_port", "devices" + str(i), str(devices_list[i]))
            command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + str(devices_list[i]) + " --no-reset --session-override"
            command_list.append(command)
        return command_list

    def start_server(self, i):
        self.dos.execute_cmd(i)

    def start_server_thread(self):
        self.kill_node_server()
        for i in self.create_command_list():
            self.appium_start = threading.Thread(target=self.start_server, args=(i,))
            self.appium_start.start()
        time.sleep(10)


if __name__ == "__main__":
    se = Server()
    devices_list = se.get_devices()
    se.connect_device(devices_list)
    # se.start_server_thread()