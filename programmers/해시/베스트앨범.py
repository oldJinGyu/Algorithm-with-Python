import sys
input=sys.stdin.readline

genres=list(input().split())
plays=list(map(int,input().split()))

def solution(genres, plays):
    answer = []
    dic={}
    dicnt={}
    names=[]
    lst=[]
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]]=[[genres[i],i,plays[i]]]
            dicnt[genres[i]]=plays[i]
            names.append(genres[i])
        else:
            dic[genres[i]].append([genres[i],i,plays[i]])
            dicnt[genres[i]]+=plays[i]
    
    for i in range(len(names)):
        for j in range(len(dic[names[i]])):
            dic[names[i]][j].append(dicnt[names[i]])
            lst.append(dic[names[i]][j])
            
    lst=sorted(lst, key=lambda x: (x[3],x[2]), reverse=True)
    answer.append(lst[0][1])
    current=lst[0][0]
    count=1
    
    for i in range(1,len(lst)):
        if count==2 and current==lst[i][0]:
            continue
        if current==lst[i][0]:
            answer.append(lst[i][1])
            count+=1
        else:
            current=lst[i][0]
            answer.append(lst[i][1])
            count=1
    
    return answer

print(solution(genres,plays))