try:
    raise FileNotFoundError ("Make your file is present")
except FileNotFoundError:
    print("File not found")
    raise #to determine whether exception is raised or not
