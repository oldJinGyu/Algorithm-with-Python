import sys

n = int(input())
j = 1

list = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)
for i in list:
    print("Case #%d: %d" %(j, i))
    j += 1