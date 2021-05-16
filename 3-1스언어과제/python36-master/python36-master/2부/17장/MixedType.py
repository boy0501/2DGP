# -*- coding: utf-8 -*-
import smtplib
import mimetypes

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#global value
host = "smtp.test.com" #your smtp address
htmlFileName = "logo.html"
imageFileName = "logo.gif"

senderAddr = "test@send.com"     #������ ��� email �ּ�.
recipientAddr = "test@rec.com"   #�޴� ��� email �ּ�.

#create MMIMEBase 
msg = MIMEBase("multipart", "mixed")

msg['Subject'] = "Test email in Python 3.0"
msg['From'] = senderAddr
msg['To'] = recipientAddr

#Make MIMEType
htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(htmlFD.read(), _charset = 'UTF-8' )
htmlFD.close()

imageFD = open(imageFileName, 'rb')
ImagePart = MIMEImage(imageFD.read())
imageFD.close()

# ������� mime�� MIMEBase�� ÷�� ��Ų��.
msg.attach(ImagePart)
msg.attach(HtmlPart)

#����� ÷�� ���Ͽ� ���� ������ �߰� ��Ų��.
msg.add_header('Content-Disposition','attachment',filename=imageFileName)

msg['Subject'] = "test python email"
msg['From'] = senderAddr
msg['To'] = recipientAddr


#������ �߼��Ѵ�.
s = smtplib.SMTP(host)
s.connect()
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()
