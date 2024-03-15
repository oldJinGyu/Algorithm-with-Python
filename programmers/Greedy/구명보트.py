import sys
input=sys.stdin.readline

people=list(map(int,input().split()))
limit=int(input())

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    p=dict()
    t=0
    for i in range(len(people)):
        p[i]=people[i]
    while p:
        pkeys=[]
        for i in p:
            if t+p[i]<=limit:
                pkeys.append(i)
                t+=p[i]
            else:
                answer+=1
                t=0
                break
        for i in pkeys:
            p.pop(i)
            
    if t!=0:
        answer+=1
    return answer
print(solution(people,limit))