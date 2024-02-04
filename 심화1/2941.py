import re

list=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
for i in list:
    s=re.sub(i,"*",s)
print(len(s))