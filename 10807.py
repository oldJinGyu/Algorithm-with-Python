import sys
j = 0
input()
list = map(int, sys.stdin.readline().split())
n = int(input())
for i in list:
    if i == n:
        j += 1
print(j)