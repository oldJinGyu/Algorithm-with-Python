import sys, heapq
input=sys.stdin.readline

operations=list(input().split())

def solution(operations):
    q=[]
    for i in operations:
        op=i[0]         #명령어 추출
        num=int(i[2:])  #숫자 추출
        if op=="I":
            heapq.heappush(q,num)       #기본적으로 최소힙을 사용
        elif op=="D" and num==-1:       #최소힙이기 때문에 최솟값 구하기 쉬움
            if q:
                heapq.heappop(q)
        else:
            if q:
                for j in range(len(q)): #최댓값을 구할 때는 최대힙으로 변경후
                    q[j]*=-1            #
                heapq.heapify(q)        #여기까지가 최대힙 만드는 과정
                heapq.heappop(q)        #최댓값 제거
                for j in range(len(q)): #다시 최소힙으로 변경
                    q[j]*=-1            #
                heapq.heapify(q)        #여기까지가 최소힙 만드는 과정
    if q:                               #q에 값이 있으면 max,min추출 
        return [max(q),min(q)]
    else:                               #q가 빈 리스트면 [0,0] 반환
        return [0,0]

print(solution(operations))