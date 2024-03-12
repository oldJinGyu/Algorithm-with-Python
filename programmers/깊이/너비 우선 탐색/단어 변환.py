import sys
from collections import deque
input=sys.stdin.readline

begin=input().rstrip()
target=input().rstrip()
words=list(input().split())

def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)
    
def bfs(begin, target, words):
    q=deque()
    q.append([begin,0])
    
    while q:
        now, cnt=q.popleft()
        
        if now==target:
            return cnt
        
        for word in words:
            count = 0
            for i in range(len(now)): 
                if now[i] != word[i]: 
                    count += 1
                    
            if count == 1: 
                q.append([word, cnt+1])
                
print(solution(begin, target, words))