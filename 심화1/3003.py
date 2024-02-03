import sys
s = map(int, sys.stdin.readline().split())
l = [1, 1, 2, 2, 2, 8]
print(*(x-y for x,y in zip(l, s)))