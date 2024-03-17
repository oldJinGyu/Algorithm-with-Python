import sys
input=sys.stdin.readline

participant=list(input().split())
completion=list(input().split())

def solution(participant, completion):
    if len(set(participant))==len(participant):
        answer=list(set(participant)-set(completion))[0]
    else:
        par=dict()
        for i in participant:
            if i not in par:
                par[i]=1
            else:
                par[i]+=1
        for i in completion:
            par[i]-=1
        for i in par:
            if par[i]==1:
                answer=i
                break
    return answer

print(solution(participant,completion))