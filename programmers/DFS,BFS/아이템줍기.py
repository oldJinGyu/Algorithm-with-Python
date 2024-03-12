import sys
from collections import deque
input=sys.stdin.readline

rectangle=[]
for _ in range(int(input())):
    a=list(map(int, input().split()))
    rectangle.append(a)

characterX=int(input())
characterY=int(input())
itemX=int(input())
itemY=int(input())

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    op = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dq = deque()
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] == -1:
                    graph[i][j] = 1                
    
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    dq.append((cx, cy))
    
    while dq:
        x, y = dq.popleft()
        
        if x == ix and y == iy:
            answer = graph[x][y]//2
            break   
        for k in range(4):
            nx, ny = x + op[k][0], y + op[k][1]
            
            if graph[nx][ny] == 1:
                graph[nx][ny]=graph[x][y]+1
                dq.append((nx, ny))

    return answer

print(solution(rectangle, characterX, characterY, itemX, itemY))