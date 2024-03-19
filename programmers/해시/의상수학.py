import sys
input=sys.stdin.readline

clothes=[]
for _ in range(2):
    a=list(input().split())
    clothes.append(a)
    
def solution(clothes):
    dic=dict()
    names=[]
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]]=1
            names.append(i[1])
        else:
            dic[i[1]]+=1
    
    t=dic[names[0]]+1
    for i in range(1,len(names)):
        t*=dic[names[i]]+1
        
    return t-1

print(solution(clothes))