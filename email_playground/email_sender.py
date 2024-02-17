import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

app_password = 'haxz vncw srwf mrae'

email = EmailMessage()

email['from'] = 'Yourself'
email['to'] = 'jcketterer18@gmail.com'
email['subject'] = 'Click here'

email.set_content(html.substitute(name='TinTin'),'html') #you can also use a dictionary 

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    
    smtp.login('jcketterer18@gmail.com',app_password)
    smtp.send_message(email)
    print('all good boss')