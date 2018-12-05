# 你的一个朋友生日快到了，你决定搞个恶作剧——用邮件塞满他的邮箱。
# 功能描述：首先去注册十个邮箱，然后用这十个邮箱轮流发送随机生成的邮件内容给你的朋友。调整发送的频率，以免被服务器拒绝。
# 发生554错误：554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.126.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令

sender = ''
receivers = ['']  # 接收邮件

message = MIMEText('正文内容:这是个自己的测试，不知道行不行，之前总是报554的错误', 'plain', 'utf-8')
message['From'] = Header("自己的邮箱126", 'utf-8')     # 发送者
message['To'] =  Header("自己的邮箱qq", 'utf-8')          # 接收者

subject = '正文内容:这是个自己的测试，不知道行不行，之前总是报554的错误'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(str(e))
