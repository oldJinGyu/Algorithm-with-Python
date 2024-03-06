n=int(input())
c=2;t=1;i=1
while n>t:
    t+=c
    c+=1;i+=1
if i%2==0:
    x=t-n+1
    print(i-x+1,"/",x,sep="")
else:
    x=t-n+1
    print(x,"/",i-x+1,sep="")