

# Optional Email Alert
# import smtplib
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login("yourmail@gmail.com", "password")
# server.sendmail("yourmail@gmail.com", "admin@mail.com", msg)
# server.quit()
import smtplib
from email.mime.text import MIMEText
import sys

sender_email = "manepatilvaishnavi9@gmail.com"
receiver_email = "vmanepatil8@gmail.com"

app_password = "ddab yqal hfkh cdzi"

message = "Docker Guardian Test Alert"

msg = MIMEText(message)

msg['Subject'] = "Docker Guardian Alert"
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender_email, app_password)

    server.sendmail(
        sender_email,
        receiver_email,
        msg.as_string()
    )

    server.quit()

    print("Email Sent Successfully")

except Exception as e:
    print("Error:", e)
