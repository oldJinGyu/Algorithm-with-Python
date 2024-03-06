import sys
input=sys.stdin.readline
n=int(input())
def find(n,n2):
    count=0
    l=[True for _ in range(n2+1)]
    l[0]=l[1]=False
    p=2
    while p**2<=n2:
        if l[p]==True:
            for i in range(p**2,n2+1,p):
                l[i]=False
        p+=1
    for i in range(n+1,n2+1):
        if l[i]:
            count+=1
    return count
while n!=0:
    n2=2*n
    print(find(n,n2))
    n=int(input())