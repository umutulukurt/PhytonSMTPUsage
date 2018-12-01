

import smtplib

msg = "a"
fromemail= "xxx@gmail.com"
pwd = "xxx"
targetmail = "xxx@gmail.com"
port=587
Hello = " # The /n separates the message from the headers"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromemail, pwd)
text = msg.as_string()
server.sendmail(frommail, targetmail, text)
server.quit()


