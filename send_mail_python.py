import smtplib

content = "hello i m sending email using python"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.ehlo()

server.starttls()
server.login("pinnintirevati999@gmail.com", "password")
server.sendmail("pinnintirevati999@gmail.com", "pinnintirevati999@gmail.com", content)
server.quit()
