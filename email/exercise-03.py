import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv("exercise/email/.env")


def send_email(to, subject, message):
  try:
    email_host     = os.environ.get("EMAIL_HOST")
    email_username = os.environ.get("EMAIL_USERNAME")
    email_password = os.environ.get("EMAIL_PASSWORD")

    if email_username is None or email_password is None:
        print("Did you set email address and password correctly?")
        return False

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_username
    msg['To'] = to
    msg.set_content(message)

    # send email
    with smtplib.SMTP(email_host, 587) as smtp:
      smtp.starttls()
      smtp.login(email_username, email_password)
      smtp.send_message(msg)
    
    return True
  except Exception as e:
    print("Problem during send email")
    print(str(e))

  return False


send_email("daghan.altunsoy@gmail.com", "test-1", "test message 1")