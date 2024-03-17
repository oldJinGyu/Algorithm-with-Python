import sys
input=sys.stdin.readline

nums=list(map(int, input().split()))

def solution(nums):
    
    a=len(set(nums))
    n=len(nums)//2
    
    return a if a<=n else n

print(solution(nums))