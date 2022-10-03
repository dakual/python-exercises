import smtplib, os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv("exercise/email/.env")

email_host     = os.environ.get("EMAIL_HOST")
email_port     = os.environ.get("EMAIL_PORT")
email_username = os.environ.get("EMAIL_USERNAME")
email_password = os.environ.get("EMAIL_PASSWORD")

subject        = "An example of boarding pass"
sender_email   = email_username
receiver_email = "daghan.altunsoy@gmail.com"
filename       = "test.db"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
body = "This is an example of how you can send a boarding pass in attachment with Python"
message.attach(MIMEText(body, "plain"))

# Add attachment
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
message.attach(part)

# send your email
with smtplib.SMTP(email_host, email_port) as server:
  server.starttls()
  server.login(email_username, email_password)
  server.sendmail(
      sender_email, receiver_email, message.as_string()
  )

print('Sent') 