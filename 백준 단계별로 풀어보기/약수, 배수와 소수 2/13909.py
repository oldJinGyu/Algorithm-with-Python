import sys
input=sys.stdin.readline
n=int(input())
c=0
while c**2<=n:
    c+=1
print(c-1)
    