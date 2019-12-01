import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '111@qq.com'
receivers = ['222@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python</p>
<p><a href="http://www.163.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("服务器中心", 'utf-8')
message['To'] =  Header("好好学生", 'utf-8')

subject = 'Python SMTP '
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpObj.set_debuglevel(1)
    smtpObj.login("111@qq.com", "11111")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
