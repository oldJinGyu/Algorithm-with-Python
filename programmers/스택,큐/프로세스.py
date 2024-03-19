import sys
input=sys.stdin.readline

priorities=list(map(int,input().split()))
location=int(input())

def solution(priorities, location):
    answer=0
    lst=[i for i in range(len(priorities))] #순서를 관찰하기 위해 만듬
    while priorities:
        m=max(priorities)
        a=priorities.pop(0)
        num=lst.pop(0)
        p=True
        if a!=m:
            priorities.append(a)
            lst.append(num)
            p=False
        if p:
            answer+=1
            if num==location:
                break
    return answer

print(solution(priorities,location))