import sys, heapq
input=sys.stdin.readline

scoville=list(map(int,input().split()))
k=int(input())

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0]>=k:
            break
        
        if len(scoville)==1 and scoville[0]<k:
            return -1
            
        if len(scoville)>1:
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            heapq.heappush(scoville,a+b*2)
            answer+=1
        
    return answer

print(solution(scoville,k))