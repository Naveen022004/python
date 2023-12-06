import re
password=input("Enter password")
pattern = '[0-9a-z]'
r=re.search(pattern,password)
print(r)