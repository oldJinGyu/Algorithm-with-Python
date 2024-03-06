import sys

input=sys.stdin.readline
l={}
for _ in range(int(input())):
    n,f=map(str, input().split())
    if f=='leave':
        del l[n]
    else:
        l[n]=0
l=sorted(l.keys(), reverse=True)
for i in l:
    print(i)