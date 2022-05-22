import smtplib, ssl
import os

port = 465
smtp_server = os.environ.get("SMTP_ADDRESS")
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")

message = """\
    Subject: keepalive_jfrog job status

    keepalive_jfrog job completed now.
"""

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, USER_EMAIL, message)
