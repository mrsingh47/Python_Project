import datetime
import time
name=input("Enter your name \n")
edate= datetime.datetime.now()
for i in range(10):
    edate = datetime.datetime.now()
    print(name,edate)
    time.sleep(1)