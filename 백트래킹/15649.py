import sys
input=sys.stdin.readline
n,m=map(int,input().split())
def deep(n,m):
    if m==1:
        l=[]
        for i in range(1,n+1):
            l.append([i])
        return l
    l=[]
    deeps=deep(n,m-1)
    for i in deeps:
        for j in range(1,n+1):
            t=[]
            if j in i:
                continue
            else:
                t=i[:]
                t.append(j)
                l.append(t)
    return l
for i in deep(n,m):
    print(*i)