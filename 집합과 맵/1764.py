import sys

input=sys.stdin.readline
n,m=map(int,input().split())
a=set();b=set()
for _ in range(n):
    a.add(input().rstrip())
for _ in range(m):
    b.add(input().rstrip())
r=sorted(list(a&b))
print(len(r))
for i in r:
    print(i)