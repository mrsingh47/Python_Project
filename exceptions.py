try:
    no=int(input("Enter your lucky no\n"))
    zero=0
    print(no/zero)

except ZeroDivisionError:
    print("You can't divide a no by zero")
except:
    print("Exception is there")
finally:
    print("Thank you for using our application")