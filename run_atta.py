#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Ranxf

"""发送带附件的邮件"""
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

# 接收人
receiver = "thakral@126.com"

# ----------2.编辑邮件的内容------
# 读文件
file_path = "result.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender
# 发件人
msg["to"] = receiver
# 收件人
msg["subject"] = "这是我的主题"
# 主题
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)
# ----------3.发送邮件------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    # 连服务器
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string()) # 发送
    smtp.quit()