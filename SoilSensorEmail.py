import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

from_email_addr = "2867218760@qq.com"
from_email_pass = "waompooggbgeddbd"
to_email_addr = "3025977257@qq.com"

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def check_status():
	if GPIO.input(channel):
		return "Please water your plant"
	else:
		return "Water not needed"


def send_email(status):
	msg = EmailMessage()
	msg.set_content(status)
	msg["From"] = from_email_addr
	msg["To"] = to_email_addr
	msg["Subject"] = "Plant Status"
	
	server = smtplib.SMTP_SSL("smtp.qq.com", 465)
	server.login(from_email_addr, from_email_pass)
	server.send_message(msg)
	server.quit()

def main():
	while True:
		status = check_status()
		send_email(status)
		time.sleep(10800)

	GPIO.cleanup()
	

main()
