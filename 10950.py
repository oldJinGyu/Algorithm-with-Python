t = int(input())
list = []
for i in range(t):
    x, y = map(int, input().split())
    list.append(x+y)
for i in list:
    print(i)