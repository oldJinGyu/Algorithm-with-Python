import sys
input=sys.stdin.readline

phone_book=list(input().split())

def solution(phone_book):
    answer = True
    nums=dict()
    for i in phone_book:
        for j in range(1,len(i)):
            if i[:j] not in nums:
                nums[i[:j]]=1
                
    
    for i in phone_book:
        if i in nums:
            return False
        
    return answer

solution(phone_book)
