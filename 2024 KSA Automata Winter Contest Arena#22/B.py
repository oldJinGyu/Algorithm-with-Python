import sys
input=sys.stdin.readline
x=list(input().rstrip())
s=['K','S','A'];c=0;j=0
for i in x:
    if i==s[j%3]:
        j+=1
    else:
        c+=1
print(c*2)