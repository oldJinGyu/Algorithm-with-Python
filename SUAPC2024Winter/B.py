import sys
input=sys.stdin.readline

n=int(input())
t=[];m=[]
for _ in range(n):
    x,y=map(int,input().split())
    t.append([x,y])
for i in range(len(t)):
    for j in range(i+1,len(t)):
        for k in range(j+1,len(t)):
            x1,y1=t[i][0],t[i][1]
            x2,y2=t[j][0],t[j][1]
            x3,y3=t[k][0],t[k][1]
            if x1==x2==x3 or y1==y2==y3:
                continue
            s=(abs(x1*y2+x2*y3+x3*y1-x1*y3-x3*y2-x2*y1))/2
            a12=((x2-x1)**2+(y2-y1)**2)**0.5
            a13=((x3-x1)**2+(y3-y1)**2)**0.5
            a23=((x3-x2)**2+(y3-y2)**2)**0.5
            m.append(s*2/a12)
            m.append(s*2/a13)
            m.append(s*2/a23)
minh="{:.7f}".format(min(m))
print(minh)