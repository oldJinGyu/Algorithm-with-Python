import sys, math
input=sys.stdin.readline
a=[];b=[]
n=int(input())
for _ in range(n):
    a.append(int(input()))
for i in range(1,len(a)):
    b.append(a[i]-a[i-1])
b=list(set(b))
gcd = b[0]
for num in b[1:]:
    gcd = math.gcd(gcd, num)
print((a[n-1]-a[0])//gcd+1-len(a))