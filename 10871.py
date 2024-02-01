import sys

x, n = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))

for i in range(x):
    if num[i] < n:
        print(num[i], end = " ")