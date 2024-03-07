import sys
input=sys.stdin.readline

distance=int(input())
rocks=list(map(int,input().split()))
n=int(input())

rocks.append(distance)
rocks.sort()
start,end=0,distance
minvalue=1e9
while start<=end:
    mid=(start+end)//2
    rm_cnt=0
    s=0
    for rock in rocks:
       if rock-s<mid:
           rm_cnt+=1
       else:
           s=rock
    if rm_cnt==n:
        minvalue=min(mid,minvalue)
    if rm_cnt>n:
        end=mid+1
    else:
        start=mid-1
print(minvalue)