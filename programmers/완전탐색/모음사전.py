import sys
input=sys.stdin.readline

word=input().rstrip()

def solution(word):
    answer=[0]
    alpha=['A','E','I','O','U']
    result=[]
    def back(answer):
        if ''.join(result) == word:
            return True  
        if len(result) == 5:
            return False 
        for i in range(5):
            result.append(alpha[i])
            answer[0] += 1
            if back(answer):  
                return True
            result.pop()
    back(answer)      
    return answer[0]

print(solution(word))