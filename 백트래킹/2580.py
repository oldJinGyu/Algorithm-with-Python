import sys
input=sys.stdin.readline
lst=[list(map(int,input().split())) for _ in range(9)]
blank=[]
for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            blank.append((i, j))
def checkrow(x, num):
    for i in range(9):
        if num==lst[x][i]:
            return False
    return True
def checkcol(x,num):
    for i in range(9):
        if num==lst[i][x]:
            return False
    return True
def checkbox(x,y,num):
    for i in range(3):
        for j in range(3):
            if num==lst[x//3*3+i][y//3*3+j]:
                return False
    return True
def dfs(n):
    if n==len(blank):
        for i in lst:
            print(*i)
        return
    
    for i in range(1,10):
        x=blank[n][0]
        y=blank[n][1]
        
        if checkbox(x,y,i) and checkcol(y,i) and checkrow(x,i):
            lst[x][y]=i
            dfs(n+1)
            lst[x][y]=0
            
dfs(0)