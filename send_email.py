import smtplib
from email.message import EmailMessage

from_email_addr = "2867218760@qq.com"
from_email_pass = "waompooggbgeddbd" 
to_email_addr = "3025977257@qq.com"

msg = EmailMessage()
msg.set_content("Hello from Raspberry Pi")
msg["From"] = from_email_addr
msg["To"] = to_email_addr
msg["Subject"] = "TEST EMAIL"


server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(from_email_addr, from_email_pass)
server.send_message(msg) 
server.quit() 

print("Email sent！")
