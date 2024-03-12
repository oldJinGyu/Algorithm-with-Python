import sys
import copy
from collections import deque
input=sys.stdin.readline

game_board=[]
table=[]
for _ in range(6):
    game_board.append(list(map(int, input().split())))
    
for _ in range(6):
    table.append(list(map(int, input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def change(lst1, lst2):
    x=lst1[0][0]-lst2[0][0]
    y=lst1[0][1]-lst2[0][1]
    
    for i in range(len(lst2)):
        lst2[i][0]+=x
        lst2[i][1]+=y
    
    return lst2

def check(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    if len(lst1)==2 or len(lst1)==1:
        return True
    
    lst1.sort()
    lst2.sort()
    c_lst2=copy.deepcopy(lst2)
    if lst1==change(lst1,c_lst2):
        return True
    c_lst2=list(map(lambda x:[x[1],-x[0]],lst2))
    c_lst2.sort()
    if lst1==change(lst1,c_lst2):
        return True
    c_lst2=list(map(lambda x:[-x[0],-x[1]],lst2))
    c_lst2.sort()
    if lst1==change(lst1,c_lst2):
        return True
    c_lst2=list(map(lambda x:[-x[1],x[0]],lst2))
    c_lst2.sort()
    if lst1==change(lst1,c_lst2):
        return True
    
    return False

def bfs(x,y,maps,lst,a,b):
    q=deque()
    q.append((x,y))
    maps[x][y]=a
    lst.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not (0<=nx<len(maps) and 0<=ny<len(maps[0])):
                continue
            if maps[nx][ny]==b:
                lst.append([nx,ny])
                maps[nx][ny]=a
                q.append((nx,ny))
    return lst

def solution(game_board, table):
    answer = 0
    gameshape=[]
    tableshape=[]
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j]==0:
                gameshape.append(bfs(i,j,game_board,[],1,0))
            if table[i][j]==1:
                tableshape.append(bfs(i,j,table,[],0,1))
    

    visited=[False]*len(tableshape)
    
    for i in range(len(gameshape)):
        for j in range(len(tableshape)):
            if check(gameshape[i],tableshape[j]) and not visited[j]:
                print(i,j)
                visited[j]=True
                answer+=len(tableshape[j])
                break
    return answer

print(solution(game_board,table))