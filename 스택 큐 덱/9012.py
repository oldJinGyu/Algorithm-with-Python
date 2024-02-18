import sys
input=sys.stdin.readline
for _ in range(int(input())):
    l=list(input().rstrip())
    s=[]
    e=False
    for i in l:
        if i=='(':
            s.append(i)
        else:
            if len(s)==0:
                e=True
            elif s.pop()!='(':
                e=True
    if len(s)!=0:
        e=True
    if e:
        print('NO')
    else:
        print('YES')