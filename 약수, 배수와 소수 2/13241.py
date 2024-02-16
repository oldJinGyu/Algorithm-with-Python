import sys
input=sys.stdin.readline
n1,n2=map(int,input().split())
a=n1
b=n2
while a!=0:
    r=b%a
    b=a
    a=r
print(n1*n2//b)