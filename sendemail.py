import smtplib
from_name = "Khadijah Brown"
to_name = "K Brown"
from_addr = 'wgs.khadijah.brown@gmail.com'
to_addr = 'khadijahabrown@hotmail.com'
subject = "Testing Lab 3"
msg = "I am testing this lab again"
message = """From: {} <{}>
To: {} <{}> 
Subject: {} 

{}
""".format(from_name, from_addr, to_name, to_addr, subject, msg)


message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
# Credentials (if needed)
username = ""
password = ""
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()