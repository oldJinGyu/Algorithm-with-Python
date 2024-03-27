import sys
input=sys.stdin.readline

numbers=list(map(int,input().split()))

def solution(numbers):
    answer = ''
    lst=[[0,0,0] for i in range(len(numbers))] 
    for i in range(len(numbers)):
        num=numbers[i]               # 3자리수와 2자리수가 있을 때 시작하는 두 수가 같으면 ex)35 358
        if 10<=num<100:              # 2자리수의 앞과 3자리수의 맨뒤를 비교해서 순서가 정해진다. 
            lst[i][0]=num*10+num//10 # 그렇기 때문에 2자리수를 2자리+앞자리로 만든다. ex)35 -> 353
            lst[i][1]=num%10         # 만든 수를 lst의 0번째에 담는다.
            lst[i][2]=num            # 이렇게 변경한 2자리와 3자리수가 같으면 2자리수의 마지막과
        elif 100<=num<1000:          # 3자리수의 마지막을 비교해야 한다. ex) 38 383 이면 8과 3을 비교
            lst[i][0]=num            # 뒷자리를 lst의 1번째에 담는다.
            lst[i][1]=num%10         # 2번째에는 원래의 수를 담는다.
            lst[i][2]=num
        elif num==1000:              # 만약 1000이면 무조건 0다음 순위이기 때문에 0과 100사이의
            lst[i][0]=99             # 아무 수나 넣는다.
            lst[i][1]=0
            lst[i][2]=num
        else:
            lst[i][0]=num*111        # 1자리 수면 111을 곱해서 넣는다 8이면 888
            lst[i][1]=lst[i][2]=num
    lst=sorted(lst, key=lambda x:(-x[0],-x[1])) # 큰 숫자가 앞에 와야하기 때문에 역순으로 정렬한다. 
    for i in range(len(numbers)):
        answer+=str(lst[i][2])
    if int(answer)==0: #결과가 "00"일 수도 있으니까 11번 테스트 
        return "0"
    return answer

print(solution(numbers))