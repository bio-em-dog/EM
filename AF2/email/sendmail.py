import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

mail_host = 'smtp.126.com'
mail_user = 'emlabaf2@126.com'
try:
    f=open('passwd.txt')
    mail_pass = f.readlines()[0].split("\n")[0]
except FileNotFoundError:
    print("no 'passwd.txt'")
    exit(0)

sender = "emlab AlphaFold2 server"
receivers = ["1014862139@qq.com"]
subject = "发件测试"

content = "ceshi\nceshi\t"

def sendEmail(cont,rece):
    
    message = MIMEText(cont, 'plain','utf-8')
    message['from'] = Header(sender, 'utf-8')
    message['To'] = ",".join(rece)
    message['Subject'] = Header(subject, 'utf-8')
    
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(mail_user, rece, message.as_string())
    smtpObj.quit()

def sendEmailAtt(cont,rece,atts): #(str, list, list)
    message = MIMEMultipart()
    message['from'] = Header(sender, 'utf-8')
    message['To'] = ",".join(rece)
    message['Subject'] = Header(subject, 'utf-8')
    
    message.attach(MIMEText(cont, 'plain', 'utf-8'))
    
    if len(atts) >=1:
        for i in atts:
            att = MIMEApplication(open(i,'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=i)
            message.attach(att)
        
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(mail_user, rece, message.as_string())
    smtpObj.quit()

#sendEmail(content, receivers)
sendEmailAtt(content, receivers, ["aff.txt"])
        

