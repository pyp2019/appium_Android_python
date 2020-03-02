
"""
import smtplib
from email.mime.text import MIMEText
# # 邮箱服务器
# mail_host = 'smtp.qq.com'
# # 邮箱端口
# # MAIL_PORT = 465
# # 邮箱协议 SSL/TSL
# # MAIL_USE_SSL = True
# # MAIL_USE_TSL = False
# # 发送方的邮箱
# mail_user = '1134636122@qq.com'
# mail_pass = 'pepabcvjvvesbaac'
#
# mail_postfix = "qq.com"
#
#
# def send_mail(to_list, sub, reportpath):
#     ""
#     to_list: 收件人
#     sub: 主题
#     reportpath: 报告
#     ""
#     file = open(reportpath, 'rb')
#     content = ""
#     for line in file.readlines():
#         content = content + line.replace("class='hiddenRow'", "")
#
#     me = "TestCenter" + "<" + mail_user + ">"
"""
# 邮箱服务器
import datetime
import os

MAIL_SERVER = 'smtp.qq.com'
# 邮箱端口
MAIL_PORT = 465
# 邮箱协议 SSL/TSL
MAIL_USE_SSL = True
MAIL_USE_TSL = False

# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '1134636122@qq.com'
password = 'pepabcvjvvesbaac'

# 收信方邮箱
# to_addr = 'xxx@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'


def send_mail(to, sub, reportpath):
    """
    to: 接收方邮箱
    sub ： 主题
    reportpath: 发送的html
    """
    to_addr = to
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(html 为html页面)，第三个参数为编码

    with open(reportpath, 'r', encoding='UTF-8') as f:
        content = f.read()

    msg = MIMEText(content, 'html', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(sub)

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


# reportpath = file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/report/" + "login_case.html"
# with open(reportpath, 'r', encoding='UTF-8') as f:
#     content = f.read()
#
# with open("ss.html", "w", encoding='UTF-8') as f:
#     f.write(content)
# print(content)
#
# now = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
#
#
# print(now)
