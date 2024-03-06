import sys
input=sys.stdin.readline
n,m=map(int,input().split())
rs=[]
def back():
    if len(rs)==m:
        print(*rs)
        return
    for i in range(1,n+1):
        if i not in rs:
            rs.append(i)
            back()
            rs.pop()
back()