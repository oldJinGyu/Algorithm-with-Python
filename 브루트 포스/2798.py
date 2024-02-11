n,m=map(int,input().split())
s=list(map(int,input().split()))
list=[]
for i in range(n):
    for j in range((i+1),n):
        for k in range((k+1),n):
            sum=s[i]+s[j]+s[k]
            if sum<=m:
                list.append(sum)
print(max(list))