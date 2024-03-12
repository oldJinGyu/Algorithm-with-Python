import sys
from collections import deque
input=sys.stdin.readline

maps=[]
for _ in range(5):
    m=list(map(int,input().split()))
    maps.append(m)

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y,maps):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (not (0<=nx<len(maps) and 0<=ny<len(maps[0]))):
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
        
def solution(maps):
    bfs(0,0,maps)
    return maps[len(maps)-1][len(maps[0])-1] if maps[len(maps)-1][len(maps[0])-1]!=1 else -1

print(solution(maps))