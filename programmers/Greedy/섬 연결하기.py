import sys
input=sys.stdin.readline

n=int(input())
costs=[list(map(int,input().split())) for _ in range(5)]

def solution(n, costs):
    answer = 0
    cnt=1
    check=[False]*n
    check[0]=True
    while cnt<n:
        minnum=10e9
        for i in costs:
            if check[i[0]] and not check[i[1]]:
                minnum=min(i[2],minnum)
            if check[i[1]] and not check[i[0]]:
                minnum=min(i[2],minnum)
        for i in costs:
            if (check[i[0]] and not check[i[1]]) or (check[i[1]] and not check[i[0]]) :
            	if i[2]==minnum:
                    check[i[1]]=True
                    check[i[0]]=True
                    answer+=i[2]
        cnt+=1
            
    return answer

print(solution(n,costs))