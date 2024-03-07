import sys
input=sys.stdin.readline
n=int(input())
times=list(map(int,input().split()))
count=times[:]
for _ in range(n):
    t=min(times)
    min_idx=times.index(t)
    times[min_idx]+=count[min_idx]
print(t)