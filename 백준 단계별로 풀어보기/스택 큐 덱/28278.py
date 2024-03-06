import sys
input=sys.stdin.readline
def stack(n,s):
    if n[0]==1:
        s.append(n[1])
    elif n[0]==2:
        if len(s)==0:
            print(-1)
        else:
            print(s.pop())
    elif n[0]==3:
        print(len(s))
    elif n[0]==4:
        if len(s)==0:
            print(1)
        else:
            print(0)
    elif n[0]==5:
        if len(s)==0:
            print(-1)
        else:
            print(s[len(s)-1])
s=[]
for _ in range(int(input())):
    n=list(map(int, input().split()))
    stack(n,s)