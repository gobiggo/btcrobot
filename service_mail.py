# -*- coding: utf-8 -*-

import smtplib
from smtplib import SMTPException

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

sender = 'slg927@gmail.com'
receivers = ['sloong@yeah.net']

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
#
# msg = "YOUR MESSAGE!"
# server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
# server.quit()

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, "1QA2WS3ED")
    server.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")

