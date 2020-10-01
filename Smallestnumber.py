#to find smallest of given 3 numbers
def smallest(a,b,c):
    d = 0
    while ( a and b and c ):
            a=a-1
            b=b-1
            c=c-1
            d=d+1
    return d
a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
c=int(input("Enter the third number\n"))
print("Minimum of three number is",smallest(a,b,c))
