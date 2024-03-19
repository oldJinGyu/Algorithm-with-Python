import sys
input=sys.stdin.readline

s=input().rstrip()

def solution(s):
    stack=[]
    for i in s:
        if i=="(":
            stack.append(i)
        elif i==")":
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

print(solution(s))