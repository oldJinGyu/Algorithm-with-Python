import sys
from collections import deque
input=sys.stdin.readline

bridge_length, weight=map(int,input().split())
truck_weights=list(map(int,input().split()))

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q=deque()
    t=0
    while q or truck_weights:
        for i in range(len(q)):          #q[[i,j]] 일 때 i는 무게를 j는 시간을 나타냄 
            q[i][1]+=1                   #한 타임 돌았기 때문에 q에 있는 모든 j를 1 늘려줌
        if q:                            
            if q[0][1]==bridge_length+1: #트럭이 다리를 지나갔으면 빼줌
                t-=q[0][0]
                q.popleft()
        if truck_weights:                #트럭이 남았고 다리에 올라갈 수 있으면 올려보냄
            n=truck_weights[0]
            if len(q)<bridge_length and t+n<=weight:
                q.append([n,1])
                t+=n
                truck_weights.pop(0)
        answer+=1
    return answer

print(solution(bridge_length,weight,truck_weights))