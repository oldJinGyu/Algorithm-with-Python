a=[list(map(int, input().split())) for _ in range(9)]
max=0
b=0;c=0
for i in range(9):
    for j in range(9):
        if max<a[i][j]:
            max=a[i][j]
            b=i;c=j
print(max)
print(b,c)