import sys
input=sys.stdin.readline
n=input()
l=list(map(int, input().split()))
lset=sorted(set(l))
num={}
for i in range(len(lset)):
    num[lset[i]]=i
for i in l:
    print(num[i],end=' ')