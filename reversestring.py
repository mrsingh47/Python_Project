def reverse(givenstring):
    string = ""
    for i in givenstring:
        string = i + string
    return string
givenstring = str(input("Enter the string\n"))
print("The original string  is : ", givenstring)
print("The reversed string is : ", reverse(givenstring))