# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------1.跟发件相关的参数------

# 发件服务器
# smtpserver = "smtp.126.com"
smtpserver = "smtp.qq.com"

# 端口
# port = 0
port = 465

# 账号
# sender = "thakral@126.com"
sender = "1637275348@qq.com"

# 密码
# psw = "02884392456"
psw = "oodcabzcdwjkbicg"

# receiver = ["xxxx@qq.com"]
# 单个接收人也可以是 list
receiver = ["1637275348@qq.com", "283017152@qq.com", "thakral@126.com"]
# 多个收件人 list 对象
# ----------2.编辑邮件的内容------
# 读文件
file_path = "result.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender
# 发件人
msg["to"] = ";".join(receiver)
# 多个收件人 list 转 str
msg["subject"] = "这是我的多用户邮件发送主题 666"
# 主题
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="result.html"'
msg.attach(att)
# ----------3.发送邮件------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    # 连服务器
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    # 登录
    smtp.sendmail(sender, receiver, msg.as_string()) # 发送
    smtp.quit()