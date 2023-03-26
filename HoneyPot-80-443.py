# GreysMatter.htb
# Alerts on Web 80 and 443


import socket
import smtplib
from email.mime.text import MIMEText

# configure email settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@gmail.com'
SMTP_PASSWORD = 'your_email_password'
EMAIL_FROM = 'your_email@gmail.com'
EMAIL_TO = 'recipient_email@example.com'

# create sockets and bind to ports 80 and 443
server_socket_80 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_80.bind(('0.0.0.0', 80))
server_socket_80.listen(1)

server_socket_443 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_443.bind(('0.0.0.0', 443))
server_socket_443.listen(1)

# wait for incoming connections on both ports
while True:
    client_socket_80, client_address_80 = server_socket_80.accept()
    # log the connection attempt
    print(f"Connection attempt from {client_address_80} on port 80")
    # send email notification
    msg = MIMEText(f"Connection attempt from {client_address_80} on port 80")
    msg['Subject'] = f"Honeypot alert: Connection attempt from {client_address_80} on port 80"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    # close the connection
    client_socket_80.close()

    client_socket_443, client_address_443 = server_socket_443.accept()
    # log the connection attempt
    print(f"Connection attempt from {client_address_443} on port 443")
    # send email notification
    msg = MIMEText(f"Connection attempt from {client_address_443} on port 443")
    msg['Subject'] = f"Honeypot alert: Connection attempt from {client_address_443} on port 443"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    # close the connection
    client_socket_443.close()
