# 你的一个朋友生日快到了，你决定搞个恶作剧——用邮件塞满他的邮箱。
# 功能描述：首先去注册十个邮箱，然后用这十个邮箱轮流发送随机生成的邮件内容给你的朋友。调整发送的频率，以免被服务器拒绝。
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.126.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令

sender = 'lk0429@126.com'
receivers = ['261173157@qq.com']  # 接收邮件

message = MIMEText('Python 邮件发送测试...', 'plain')
message['From'] = Header("菜鸟教程")
message['To'] = Header("测试")

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers,'aa')
    # smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
