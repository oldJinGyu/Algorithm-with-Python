import sys
input=sys.stdin.readline
m,n=map(int,input().split())
def find(num):
    r=[]
    l=[True for _ in range(num+1)]
    p=2
    while p**2<=num:
        if l[p]==True:
            for i in range(p**2,num+1,p):
                l[i]=False
        p+=1
    for i in range(2,num+1):
        if l[i]:
            r.append(i)
    return r
s=find(n)
for i in s:
    if i>=m:
        print(i)