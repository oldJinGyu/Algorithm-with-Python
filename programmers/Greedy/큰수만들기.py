import sys
input=sys.stdin.readline

number=input().rstrip()
k=int(input())

def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0:
        stack = stack[:-k]  # 남은 k번만큼 뒤에서부터 제거
    return ''.join(stack)

print(solution(number,k))