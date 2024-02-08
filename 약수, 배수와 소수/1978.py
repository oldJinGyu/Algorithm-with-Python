import sys
input();a=map(int, sys.stdin.readline().split());c=0
for i in a:
    list=[]
    for j in range(1,i+1):
        if i%j==0:
            list.append(j)
    if len(list)==2:
        c+=1
print(c) 