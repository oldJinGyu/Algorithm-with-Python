import sys
input=sys.stdin.readline

k = int(input())
dungeons=[]
for _ in range(5):
    x,y=map(int,input().split())
    dungeons.append([x,y])
    
def solution(k, dungeons):
    result=[]
    def dfs(n, k, cnt, b):
        if b==False or n==len(dungeons):
            result.append(cnt)
            return
        
        for i in range(n, len(dungeons)):
            if k>=dungeons[i][0]:
                k-=dungeons[i][1]
                cnt+=1
                dfs(n+1,k,cnt,True)
                k+=dungeons[i][1]
                cnt-=1
            else:
                dfs(n+1,k,cnt,False)
    dfs(0, k, 0, True)
    answer = max(result)
    return answer
print(solution(k, dungeons))