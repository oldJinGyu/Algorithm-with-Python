import sys
input=sys.stdin.readline

numbers=list(map(int, input().split()))
target= int(input())


def solution(numbers, target):
    answer = [0]
    op=[1,0]
    def dfs(n, num):
        if n==len(numbers):
            if num==target:
                answer[0]+=1
            return
        for i in op:
            if i==1:
                num+=numbers[n]
                dfs(n+1,num)
                num-=numbers[n]
            else:
                num-=numbers[n]
                dfs(n+1,num)
                num+=numbers[n]
    dfs(0,0)
    
    return answer[0]

print(solution(numbers, target))