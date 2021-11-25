# This program

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

customer_names = list()
customer_emails = list()

with open("customers.txt", "r", encoding="utf-8") as customers:
    c = customers.read()
    c = c.split("\n")
    for i in range(len(c)):
        c[i] = c[i].split(",")
    for i, j in c:
        customer_names.append(i)
        customer_emails.append(j)

from_email = "yusufsalih.2363.demir@gmail.com" # You can write your own email address
for i in range(len(customer_names)):
    email = MIMEMultipart()
    email["From"] = from_email
    email["To"] = customer_emails[i]
    email["Subject"] = "Test"
    # You can change the content of the email below.
    text = """
    Hello {}. This is a test email. You can ignore.
""".format(customer_names[i])
    email_content = MIMEText(text, "plain")
    email.attach(email_content)

    try:
        m = smtplib.SMTP("smtp.gmail.com",587)
        m.ehlo()
        m.starttls()
        m.login("","") # Enter your gmail mail address and password
        m.sendmail(email["From"],email["To"],email.as_string())
        print("Mail sent to customer successfully")
        m.close()
    except:
        sys.stderr.write("Mail sending is unsuccessful!")
        sys.stderr.flush()

print("Mail sending completed!")