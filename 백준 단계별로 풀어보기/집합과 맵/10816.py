import sys

input=sys.stdin.readline
n=int(input())
l=list(map(int, input().split()))
m=int(input())
l2=list(map(int,input().split()))
num={}
for i in l2:
    num[i]=0
for i in l:
    if i in num:
        num[i]+=1
for i in l2:
    print(num[i],end=" ")