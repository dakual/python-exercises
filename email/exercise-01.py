import smtplib

host = ""
user = ""
pasw = ""

sender    = user
receivers = ['daghan.altunsoy@gmail.com']
message   = """From: E-Ruskiy <hello@e-russkiy.com>
To: Daghan <daghan.altunsoy@gmail.com>
Subject: SMTP email example


This is a test message.
"""

try:
   smtpObj = smtplib.SMTP(host, 587)
   smtpObj.starttls()
   smtpObj.login(user, pasw)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except smtplib.SMTPException as err:
  print(err)