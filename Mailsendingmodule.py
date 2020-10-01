
import smtplib
password12=input("Enter your password:\n")
MyConnection = smtplib.SMTP('smtp.gmail.com',587)
MyConnection.starttls()
MyConnection.login(user="officialmrsingh47@gmail.com",password=password12)
mymessage = """\
Subject: Demo
hi There, Tomorrow is Your Assessment. Come be prepared..!!"""
MyConnection.sendmail("officialmrsingh47@gmail.com","pratapbhavya2000@gmail.com", mymessage)
MyConnection.close()