import sys

input=sys.stdin.readline

n,m=map(int,input().split())
s={};count=0
for _ in range(n):
    s[input()]=0
for _ in range(m):
    a=input()
    if a in s:
        count+=1
print(count)