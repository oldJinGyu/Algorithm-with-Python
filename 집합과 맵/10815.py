import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
m=int(input())
c=list(map(int,input().split()))
dict={}
for i in range(n):
    dict[num[i]]=0
for j in c:
    if j in dict:
        print(1,end=' ')
    else:
        print(0,end=' ')