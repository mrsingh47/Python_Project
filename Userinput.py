#WAP to input username and age
name = input("Enter your Name \n")
age = int(input("Enter your age in years \n"))
print('Your name is '+ name)
print('Your age is ',age)

if age>=18:
    print("User is eligible for voting")
else:
    print("User is not eligible, Go home and watch POGO!!!")


print('Thank you for using my application')
