import sys
input=sys.stdin.readline
n,m=map(int,input().split())
rs=[]
def back(s):
    if len(rs)==m:
        print(*rs)
        return
    for i in range(s,n+1):
        rs.append(i)
        back(i)
        rs.pop()
back(1)