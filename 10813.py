n, m = map(int, input().split())
list = [i for i in range(1, n+1)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    list[x], list[y] = list[y], list[x]
print(*list)