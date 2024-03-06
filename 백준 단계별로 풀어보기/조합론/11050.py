import sys
input=sys.stdin.readline
n,k=map(int,input().split())
nt=1;kt=1
for i in range(n-k+1,n+1):
    nt*=i
for i in range(1,k+1):
    kt*=i
print(nt//kt)