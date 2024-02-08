n,m=map(int,input().split())
list=[]
for i in range(n):
    if n%(i+1)==0:
        list.append(i+1)
if m>len(list):
    print(0)
else:
    print(list[m-1])