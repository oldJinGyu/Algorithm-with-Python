import sys
input=sys.stdin.readline

arr=list(map(int, input().split()))

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])
    return answer

print(solution(arr))