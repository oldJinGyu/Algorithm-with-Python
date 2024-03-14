import sys
input=sys.stdin.readline

n=int(input())
lost=list(map(int,input().split()))
reserve=list(map(int,input().split()))

def solution(n, lost, reserve):
    answer = 0
    lst=dict()
    for i in range(n+2):
        lst[i]=1
    lst[0]=0
    lst[n+1]=0
    for i in lost:
        lst[i]+=-1
    for i in reserve:
        lst[i]+=1
    for i in range(1,n+1):
        if lst[i]==0 and lst[i-1]==2:
            lst[i]+=1
            lst[i-1]-=1
        if lst[i]==0 and lst[i+1]==2:
            lst[i]+=1
            lst[i-1]-=1
        print(lst)
    for i in range(1,n+1):
        if lst[i]==1 or lst[i]==2:
            answer+=1
    return answer

print(solution(n,lost,reserve))