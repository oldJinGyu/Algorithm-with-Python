import sys
input=sys.stdin.readline
while 1:
    s=input().rstrip()
    error=False
    l=[]
    if s=='.':
        break
    for i in s:
        if i=='[' or i=='(':
            l.append(i)
        elif i==']':
            if len(l)==0:
                error=True
                break
            elif l.pop()!='[':
                error=True
                break
        elif i==')':
            if len(l)==0:
                error=True
                break
            elif l.pop()!='(':
                error=True
                break
    if len(l)!=0:
        error=True
    if error:
        print('no')
    else:
        print('yes')