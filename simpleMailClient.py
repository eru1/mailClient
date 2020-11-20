import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()

with open('password', 'r') as f:
    password = f.read()

server.login('example@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Example'
msg['To'] = 'targetmail@gmail.com'
msg['Subject'] = 'Test!'

with open('message', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'rick.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename= {filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('example@gmail.com', 'target@gmail.com', text)