import sys
input=sys.stdin.readline

tickets=[]
for _ in range(int(input())):
    start,end=input().split()
    tickets.append([start,end])
            
def solution(tickets):
    tickets=sorted(tickets, key=lambda x:x[1])
    answer = []
    answer.append('ICN')
    tlen=len(tickets)
    def dfs(n,tickets,start,lst,answer):
        if n==tlen:
            answer+=lst
            return True
        for i in range(len(tickets)):
            if start==tickets[i][0]:
                s,e=tickets[i][0],tickets[i][1]
                tickets.pop(i)
                lst.append(e)
                if dfs(n+1,tickets,e,lst,answer):
                    return True
                tickets.insert(i,[s,e])
                lst.pop(-1)
        return False
    dfs(0,tickets,'ICN',[],answer)
    return answer

print(solution(tickets))