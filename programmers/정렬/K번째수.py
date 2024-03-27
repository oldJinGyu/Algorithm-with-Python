import sys
input=sys.stdin.readline

array=list(map(int, input().split()))
commands=[]
for _ in range(3):
    commands.append(list(map(int,input().split())))

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        newarr=array[i-1:j]
        newarr.sort()
        answer.append(newarr[k-1])
    return answer

print(solution(array,commands))