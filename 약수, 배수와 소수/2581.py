m=int(input())
n=int(input())
list=[k for k in range(m,n+1)]
if list[0]==1:
    list.remove(1)
for i in range(m,n+1):
    for j in range(2,i):
        if i%j==0:
            list.remove(i)
            break
if len(list)==0:
    print(-1)
else:
    print(sum(list))
    print(min(list))