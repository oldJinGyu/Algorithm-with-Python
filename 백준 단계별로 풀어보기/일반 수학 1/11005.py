nums='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=''
n,m=map(int,input().split())
while n:
    s=nums[n%m]+s
    n=n//m
print(s)