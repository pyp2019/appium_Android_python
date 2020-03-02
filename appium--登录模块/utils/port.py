from utils.dos_cmd import DosCmd


class Port(object):
    def port_is_used(self, port_number):
        """检测端口是否占用"""
        dos = DosCmd()
        command = "netstat -ano | findstr " + str(port_number)
        result = dos.execute_cmd_result(command)
        if len(result) > 0:
            return True
        return False

    def create_port_list(self, start_port, device_list):
        """
        生成一个可用端口
        :param start_port: 起始端口号
        :param device_list: 所有
        :return: 可用端口组成的list
        """
        port_list = []
        if device_list is not None:
            while len(port_list) < len(device_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            print("生成可用端口失败")
            return None


# if __name__ == "__main__":
#     p = Port()
#     l = [1, 2, 3, 4, 5]
#     # a = p.port_is_used("80")
#     a = p.create_port_list(4699, l)
#     print(a)