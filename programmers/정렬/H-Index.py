import sys
input=sys.stdin.readline

citations=list(map(int,input().split()))

def solution(citations):
    answer = 0
    n=len(citations)
    citations.sort()
    maxm=max(citations)
    for i in range(1,maxm+1): #1편~가장 높이 인용된 수 까지
        h=i
        for j in range(len(citations)):
            num = citations[j]
            if num>=h and len(citations[j:])>=h and len(citations[:j])<=h: 
                #조건에 맞으면 answer와 h를 비교해서 큰 수 넣기
                answer=max(h, answer)
                break
    return answer

print(solution(citations))