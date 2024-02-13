n=int(input())
num=[]
for _ in range(n):
    x,y=map(int,input().split())
    num.append([y,x])
num=sorted(num)
for i in range(n):
    print(num[i][1],num[i][0])