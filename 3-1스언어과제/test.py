import smtplib
s = smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.ehlo()
s.login("ic96085137@gmail.com","tnals00..")

