import sys
from collections import deque
input=sys.stdin.readline

prices=list(map(int,input().split()))

def solution(prices):
    answer = []
    for i in range(len(prices)-1):       #마지막은 0 고정이니까 마지막 빼고 진행
        n=prices[i]                      #현재 주가
        cnt=0                            #가격 방어 시간
        for i in range(i+1,len(prices)): #현재 주가 다음 인덱스 부터 검사
            if n>prices[i]:              #주가 방어 실패시 1초 추가 후 for문 종료
                cnt+=1
                break
            cnt+=1                       #주가 방어 성공시 1초 추가
        answer.append(cnt)               
    answer.append(0)
    return answer

print(solution(prices))