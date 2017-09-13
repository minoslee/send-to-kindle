#szkrbtvolfaabehb
#8613296489829@kindle.cn
import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
_user = "734887251@qq.com"
_pwd  = "szkrbtvolfaabehb"
_to   = "8613296489829@kindle.cn"

#如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "convert"
msg["From"]    = _user
msg["To"]      = _to

#---这是文字部分---
text = MIMEText("《盗梦空间》里的陀螺最后到底停没停？",'plain','gbk')
msg.attach(text)

#---这是附件部分---
attfile = r'G:\python\zhihu\ribao\content\《盗梦空间》里的陀螺最后到底停没停？.pdf'
basename = os.path.basename(attfile)
fp = open(attfile,'rb')
att = MIMEText(fp.read(),'base64','gbk')
att['Content-Type'] = 'application/octer-stream'
att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))
encoders.encode_base64(att)
msg.attach(att)

s = smtplib.SMTP_SSL("smtp.qq.com", 465,timeout = 30)#连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)#登陆服务器
s.sendmail(_user, _to, msg.as_string())#发送邮件
s.close()