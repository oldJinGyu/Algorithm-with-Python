import sys
input=sys.stdin.readline

progresses=list(map(int,input().split()))
speeds=list(map(int,input().split()))

def solution(progresses, speeds):
    answer = []
    lst=[]
    #각 프로그램 마다 남은 시간 계산
    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i]==0:
            day=(100-progresses[i])//speeds[i]
        else:
            day=(100-progresses[i])//speeds[i]+1
        lst.append(day)
    #변수 초기화
    mnum=0
    cnt=0
    for i in range(len(lst)):
        #여기서 바로 answer에 0이 들어가기 때문에 나중에 pop해 줌
        if lst[i]>mnum:         #앞에가 되어야지만 추가가 가능하기 때문에 mnum을 설정
            answer.append(cnt)  #ex) lst가 [8,5,6,9,10,11]일 때 배포하기 위해서는 최소 8일
            mnum=lst[i]         #그러면 5 6일 인거는 이미 다 되어있어서 cnt가 3 
            cnt=1               #9를 만나면 mnum이 9로 변경 cnt가 초기화
        else:
            cnt+=1
    answer.pop(0) #for문 맨 처음 0이 추가 되기 때문에 pop한번 해줌
    answer.append(cnt) #cnt를 추가해서 마무리

    return answer

print(solution(progresses,speeds))