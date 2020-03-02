"""
    执行cmd命令
"""

import os

# 执行adb devices命令，但是没有结果
# os.system("adb devices")

# 执行adb devices命令，并收集结果
# devices = os.popen("adb devices").readlines()
# print(devices)
# print([i.replace("\tdevice\n", "") for i in devices])
# a = [i.replace("\tdevice\n", "") for i in devices if "\tdevice" in i]
# print(a)
# result = [i.replace("\tdevice", "") for i in devices if "\tdevice" in i]


class DosCmd():

    def execute_cmd_result(self, command):
        """
        执行命令并获取命令结果
        :return:
        """
        res = os.popen(command).readlines()
        result = [i.strip("\n") for i in res if i != "\n"]
        return result

    def execute_cmd(self, command):
        """执行命令"""
        os.system(command)


# if __name__ == "__main__":
#     dsc = DosCmd()
#     doc = dsc.execute_cmd_result("adb devices")
#     print(doc)