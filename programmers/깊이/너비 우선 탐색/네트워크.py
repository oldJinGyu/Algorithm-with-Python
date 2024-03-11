import sys
input=sys.stdin.readline

n=int(input())
computers=[]
for _ in range(n):
    x,y,z=map(int, input().split())
    computers.append([x,y,z])
    
def dfs(graph, v, visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j]==1 and j!=i and j+1 not in graph[i+1]:
                graph[i+1].append(j+1)
    
    visited=[False]*(n+1)
    
    for i in range(1,n+1):
        print(visited)
        if not visited[i]:
            dfs(graph, i, visited)
            answer+=1
            
    return answer

print(solution(n,computers))