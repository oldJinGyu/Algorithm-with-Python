import sys
input=sys.stdin.readline

wlist=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    wlist.append([x,y])

x=wlist[0][0]
y=wlist[0][1]
for i in range(1,len(wlist)):
    x1=wlist[i][0]
    y1=wlist[i][1]
    x2=wlist[i][1]
    y2=wlist[i][0]
    if max(x,x1)*max(y,y1)<max(x,x2)*max(y,y2):
        x=max(x,x1);y=max(y,y1)
    else:
        x=max(x,x2);y=max(y,y2)
print(x*y)