import sys
input=sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))

count=1;stack=[]

while p:
    if p[0]==count:
        p.pop(0)
        count+=1
    else:
        stack.append(p.pop(0))
    while stack and stack[-1]==count:
        stack.pop()
        count+=1
while stack:
    if stack[-1]==count:
        stack.pop()
        count+=1
    else:
        break
if not stack:
    print('Nice')
else:
    print('Sad')