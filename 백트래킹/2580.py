import sys
input=sys.stdin.readline
lst=[list(map(int,input().split())) for _ in range(9)]
v1=[[False]*9 for _ in range(9)] #열
v2=[[False]*9 for _ in range(9)] #행
v3=[[False]*9 for _ in range(9)] #박스

for i in range(9):
    for j in range(9):
        if lst[i][j]!=0:
            v1[i][lst[i][j]-1]=True
            v2[j][lst[i][j]-1]=True
            v3[i//3*3+j//3][lst[i][j]-1]=True

def back(i,j):
    if i==9:
        for x in lst:
            print(*x)
        return
    if lst[i][j]:
        back(i+(j+1)//9,(j+1)%9)
        return
    for k in range(9):
        if v1[i][k] or v2[j][k] or v3[i//3*3+j//3][k]:
            continue
        lst[i][j] = k+1
        v1[i][k]=v2[j][k]=v3[i//3*3+j//3][k]=True
        back(i+(j+1)//9,(j+1)%9)
        lst[i][j] = 0
        v1[i][k]=v2[j][k]=v3[i//3*3+j//3][k]=False

back(0,0)