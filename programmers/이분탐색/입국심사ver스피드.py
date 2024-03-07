import sys
input=sys.stdin.readline

n=int(input())
times=list(map(int,input().split()))

start=0; end=min(times)*n
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in times:
        cnt+=mid//i
    if cnt<n:
        start=mid+1
    else:
        end=mid-1
print(start)