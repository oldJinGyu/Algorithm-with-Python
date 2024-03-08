import sys
input=sys.stdin.readline

n=int(input())
wires=[]
for _ in range(n-1):
    x,y=map(int, input().split())
    wires.append([x,y])
    
def dfs(graph, v, visited, r):
        visited[v]=True
        r.append(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(graph,i,visited,r)
        return r         

def solution(n, wires):
    result=[]
    for i in range(len(wires)):
        graph=[[] for _ in range(n+1)]
        wire = wires[:i]+wires[i+1:]
        for j in wire:
            if j[1] not in graph[j[0]]:
                graph[j[0]].append(j[1])
            if j[0] not in graph[j[1]]:
                graph[j[1]].append(j[0])
        visited=[False]*(n+1)
        r=[]
        result.append(abs(len(dfs(graph,1,visited,r))-(n-len(dfs(graph,1,visited,r)))-1))
    return min(result)

print(solution(n,wires))