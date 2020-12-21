import re

name=input("File name?> ")

handle = open(name)

text=handle.read()

digits=re.findall('[0-9]+',text)

s=0

for i in digits:
  s = s + int(i)

print(s)