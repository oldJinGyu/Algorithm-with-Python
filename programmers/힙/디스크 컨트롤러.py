import sys,heapq
input=sys.stdin.readline

jobs=[]
for _ in range(3):
    a=list(map(int,input().split()))
    jobs.append(a)

def change(lst, i):                         #작업 가능한 jobs를 가장 빨리 끝낼 수 있는
    lst[i][0],lst[i][1]=lst[i][1],lst[i][0] #순서로 정렬하기 위해서 스왑한 값을 task에 넣음
    return lst[i]

def solution(jobs):
    answer = 0
    jobs.sort()
    time=0  #현재 시간
    task=[] #작업 가능 리스트
    end=0   #완료한 작업 수
    n=0     #jobs확인 순서
    while end<len(jobs):
        if task:
            t, request=heapq.heappop(task)
            if request>time:
                time=request+t
                answer+=t
            else:
                answer+=t+time-request
                time+=t
            end+=1
            for i in range(n,len(jobs)):
                if jobs[i][0]<time:
                    heapq.heappush(task,change(jobs,i))
                    n+=1
                else:
                    break
        else:
            heapq.heappush(task,change(jobs,n))
            n+=1
                
    return answer//len(jobs)

print(solution(jobs))