import re

list=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
count=0
for i in list:
    count+=s.count(i)
    s=re.sub(i,"",s)
print(count+len(s))