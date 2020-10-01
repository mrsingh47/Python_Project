import pyqrcode
import png
email="pratapbhavya2000@gmail.com"
mobileno = "8587871159"
github="https://github.com/mrsingh47"
myqrcode=pyqrcode.create(email+"\n"+mobileno+"\n"+github)
myqrcode.svg("mydetails1.svg")
myqrcode.png("mydetails1.png")
print("Congo, you have your QR code now")
