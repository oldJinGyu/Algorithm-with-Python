n,m=map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(m):
    for j in range(n):
        a[i][j]+=b[i][j]
for i in a:
    print(*i)
    