import sys
input=sys.stdin.readline
t=int(input())
num=[int(input()) for _ in range(t)]
n=max(num)
def find(n):
    l=[True]*int(n+1)
    for p in range(2,n+1):
        if l[p]==True:
            for i in range(p**2,n+1,p):
                l[i]=False
    return l
l=find(n)
for i in num:
    c=0
    for j in range(2,i//2+1):
        if l[j] and l[i-j]:
            c+=1
    print(c)