import sys
input=sys.stdin.readline

numbers=list(map(int,input().split()))

def solution(numbers):
    answer = ''
    lst=[[0,0,0,0] for i in range(len(numbers))] 
    #0번 인덱스 백의 자리 1번 십의 자리 2번 일의 자리 3번 숫자
    for i in range(len(numbers)):
        if numbers[i] >=10 and numbers[i]<100:
            lst[i][0]=numbers[i]//10
            lst[i][1]=numbers[i]//10
            lst[i][2]=numbers[i]%10
            lst[i][3]=numbers[i]
        elif numbers[i] >=100:
            lst[i][0]=numbers[i]//100
            lst[i][1]=numbers[i]%10
            lst[i][2]=numbers[i]%100
            lst[i][3]=numbers[i]
        else:
            lst[i][0]=lst[i][1]=lst[i][2]=lst[i][3]=numbers[i]=numbers[i]
    lst.sort(reverse=True)
    print(lst)
    for i in range(len(numbers)):
        answer+=str(lst[i][3])
    return answer

print(solution(numbers))