a=[list(input()) for _ in range(5)]
str=""
for i in range(15):
    for j in range(5):
        if i <len(a[j]):
            str+=a[j][i]
print(str)