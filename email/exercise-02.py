import smtplib
from email.message import EmailMessage

host = ""
user = ""
pasw = ""

msg = EmailMessage()
msg['Subject'] = "subject"
msg['From']    = user
msg['To']      = "daghan.altunsoy@gmail.com"
msg.set_content("test email")

# send your email
with smtplib.SMTP(host, 587) as smtp:
  smtp.starttls()
  smtp.login(user, pasw)
  smtp.send_message(msg)
  smtp.close()

  print("Successfully sent email")
