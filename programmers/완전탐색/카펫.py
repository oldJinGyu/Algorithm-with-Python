import sys
input=sys.stdin.readline

x,y=map(int,input().split())
def solution(brown, yellow):
    answer=[]
    s=brown+yellow
    x=s;y=3
    while x>=y:
        x=s//y
        if x*y==s and (x+y-1)*2-2==brown:
            answer.append(x)
            answer.append(y)
            break
        y+=1
    return answer
print(solution(x,y))