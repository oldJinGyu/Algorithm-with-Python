import sys

input=sys.stdin.readline
n,m=map(int, input().split())
p={};rp={}
for i in range(1,n+1):
    s=str(input().rstrip())
    p[str(i)]=s
    rp[s]=str(i)
for _ in range(m):
    a=str(input().rstrip())
    if a in p:
        print(p[a])
    elif a in rp:
        print(rp[a])