import smtplib
from email import message
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


from_addr='raisudip0005@gmail.com'
to_addr='raisudip05@gmail.com'
subject='From Python'
content='This is body'

msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']=subject
body =MIMEText(content,'plain')
msg.attach(body)

filename='test.txt'
with open(filename,'r') as f:
    attachment=MIMEApplication(f.read(), Name=basename(filename))
    attachment['Content-Disposition']='attachement; filename="{}"'.format(basename(filename))
msg.attach(attachment)
server=smtplib.SMTP_SSL('smtp.gmail.com')
server.login(from_addr,'helpmejesus1')
server.send_message(msg,from_addr=from_addr,to_addrs=[to_addr])
