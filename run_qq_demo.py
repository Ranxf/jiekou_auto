#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Ranxf
# coding:utf-8

"""QQ 邮箱"""
import smtplib
from email.mime.text import MIMEText
# ----------1.跟发件相关的参数------
# smtpserver = "smtp.163.com"
# 发件服务器
smtpserver = "smtp.qq.com"
port = 465
# 端口
sender = "1637275348@qq.com"
# 账号
psw = "oodcabzcdwjkbicg"
# 密码
receiver = "1637275348@qq.com"
# 接收人
# ----------2.编辑邮件的内容------
subject = "这个是主题 QQ"
body = '<p>这个是发送的 QQ 邮件</p>'
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "1637275348@qq.com"
msg['subject'] = subject
# 定义邮件正文为 html 格式
# ----------3.发送邮件------
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
smtp = smtplib.SMTP_SSL(smtpserver, port)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
# 连服务器
# 登录
# 发送
# 关闭