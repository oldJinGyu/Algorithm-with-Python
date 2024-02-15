import sys
input=sys.stdin.readline
s=input().rstrip()
a=[]
for i in range(len(s)):
    for j in range(1,len(s)+1-i):
        a.append(s[i:i+j])
print(len(list(set(a))))