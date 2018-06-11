#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Ranxf

"""126邮箱"""
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
# ----------1.跟发件相关的参数------
smtpserver = "smtp.126.com"
# 发件服务器
port = 0
# 端口
sender = "thakral@126.com"
# 账号
psw = "02884392456"
# 密码
receiver = "1637275348@qq.com"
# 接收人
# ----------2.编辑邮件的内容------
subject = "这个是主题 126 test"
body = '<p>这个是发送的 126 邮件</p>'  # 定义邮件正文为 html 格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "1637275348@qq.com"
msg['subject'] = subject
# ----------3.发送邮件------
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
# 连服务器
smtp.login(sender, psw)
# 登录
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
# 关闭