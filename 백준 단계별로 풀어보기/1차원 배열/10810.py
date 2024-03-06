n, m = map(int, input().split())
list = [0]*n
for x in range(m):
    i, j, k = map(int, input().split())
    list[i-1:j] = [k]*(j-i+1)
print(*list)