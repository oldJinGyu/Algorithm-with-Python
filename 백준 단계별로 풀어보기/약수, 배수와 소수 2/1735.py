import sys
input=sys.stdin.readline
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a=b2*a1+b1*a2;b=b1*b2
if a>b:
    A=a;B=b
else:
    A=b;B=a
while B!=0:
    r=A%B
    A=B
    B=r
print(a//A,b//A)