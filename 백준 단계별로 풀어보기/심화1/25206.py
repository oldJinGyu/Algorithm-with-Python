list=['A+','A0','B+','B0','C+','C0','D+','D0']
g=[]
h=[]
for _ in range(20):
    a,b,c = input().split()
    count=4.5
    if c!='F':
        for i in list:
            if str(c)==i:
                g.append(count*float(b))
                h.append(float(b))
            count-=0.5
    elif c=='F':
        g.append(0)
        h.append(float(b))
print(f"{sum(g)/sum(h):.6f}")