#regular expressions
import re

txt = "The rain in the spain"
x = re.search("^The.*spain$",txt)
y = re.search("^[A-U]",txt)
print(x)
print(y)