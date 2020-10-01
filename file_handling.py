def reader():
    f = open("Demofile.txt", "r")
    print(f.read())
    f.close()

inputdata=input("Enter your message\n")
g = open("Demofile.txt", "a")
g.writelines(inputdata)
g.close()
reader()
