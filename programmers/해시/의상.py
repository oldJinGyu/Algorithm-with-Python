import sys
input=sys.stdin.readline

clothes=[]
for _ in range(2):
    a=list(input().split())
    clothes.append(a)

def op(lst):
    t=lst[0]
    for i in range(1,len(lst)):
        t*=lst[i]
    return t

def solution(clothes):
    answer = [0]
    dic=dict()
    names=[]
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]]=1
            names.append(i[1])
        else:
            dic[i[1]]+=1
    print(dic)
    
    result=[]
    def back(n):
        if len(result)==len(dic):
            return
        for i in range(n,len(names)):
            result.append(dic[names[i]])
            answer[0]+=op(result)
            back(i+1)
            result.pop()
    
    back(0)
    
    return answer[0]

print(solution(clothes))