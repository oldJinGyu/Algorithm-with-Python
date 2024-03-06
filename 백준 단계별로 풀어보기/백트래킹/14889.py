import sys
input=sys.stdin.readline

N=int(input())
m=N//2
tlst=[list(map(int, input().split())) for _ in range(N)]
def cal(alst,blst):
    suma=sumb=0
    for i in range(m):
        for j in range(m):
            suma+=tlst[alst[i]][alst[j]]
            sumb+=tlst[blst[i]][blst[j]]
    return abs(suma-sumb)
def dfs(n,alst,blst):
    global ans
    if n==N:
        if len(alst)==len(blst):
            ans=min(ans, cal(alst,blst))
        return
    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])
ans=1e9
dfs(0,[],[])
print(ans)