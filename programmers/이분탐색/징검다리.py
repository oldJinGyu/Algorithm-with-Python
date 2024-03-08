import sys
input=sys.stdin.readline

distance=int(input())
rocks=list(map(int,input().split()))
n=int(input())
answer=0
rocks.append(distance)
rocks.sort()
start,end=0,distance
minlist=[]
while start<=end:
    mid=(start+end)//2
    remove_cnt=0
    current=0
    min_distance=1e9
    for rock in rocks:
        diff=rock-current
        if diff<mid:
            remove_cnt+=1
        else:
            current=rock
            min_distance=min(min_distance, diff)
    if remove_cnt==n:
        minlist.append(min_distance)
    if remove_cnt>n:
        end=mid-1
    else:
        start=mid+1
print(minlist)