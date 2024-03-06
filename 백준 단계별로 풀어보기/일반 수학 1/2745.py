n,m=input().split()
t=0
count=1
for i in n:
    if ord(i)>=65:
        num=ord(i)-55
    else:
        num=int(i)
    t += num*(int(m)**(len(n)-count))
    count+=1
print(t)