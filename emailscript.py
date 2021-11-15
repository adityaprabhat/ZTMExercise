import smtplib                                          #Gives methods to initialize SMTP server
from email.message import EmailMessage

email = EmailMessage()

# print(type(email))
email['from'] = 'Reverse Flash'
email['to'] = 'adityaprbht@gmail.com'
email['subject'] = 'Problems in the Negative Speed Force'

email.set_content('Issues occuring in Neg Speed Force.Please check out')

with smtplib.SMTP(host = "smtp.gmail.com", port= 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.send_message(email)

        print("done!")