list = []
for _ in range(10):
    a = int(input())
    b = a%42
    list.append(b)

list = set(list)
print(len(list))
    