n=int(input())
while n!=-1:
    list=[]
    for i in range(1,n):
        if n%i==0:
            list.append(i)
    if sum(list)==n:
        print(n,"="," + ".join(str(i) for i in list))
    else:
        print('%d is NOT perfect.'%(n))
    n=int(input())