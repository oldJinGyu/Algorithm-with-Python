import sys
input=sys.stdin.readline

name=input().rstrip()

def solution(name):
    answer = 0
    for i in name:
        cnt=ord(i)
        if cnt<=77:
            answer+=cnt-65
        else:
            answer+=91-cnt
    startA=0
    endA=0
    for i in range(1,len(name)):
        if name[i]=='A':
            startA+=1
        else:
            break
    for i in range(len(name)-1,0,-1):
        if name[i]=='A':
            endA+=1
        else:
            break
    
    midA=0
    check=False
    start=False
    lastAidx=-100
    for i in range(1,len(name)):
        if name[i]!='A':
            check=True
        if check and name[i]=='A' and midA==0:
            midA=i
            start=True
        if start and name[i]!='A':
            lastAidx=i-1
            break
    
    check=False
    start=False
    endA2=-100
    Aidx=0
    for i in range(len(name)-1,0,-1):
        if name[i]!='A':
            check=True    
        if check and name[i]=='A' and endA2==-100:
            endA2=i
            start=True
        if start and name[i]!='A':
            Aidx=i
            break
        
    if list(name)==['A']*len(name):
        pass
    elif startA>=endA:
        a=answer
        answer=min(a+(midA-1)*2+len(name)-lastAidx-1,a+len(name)-(startA+1),a+Aidx+(len(name)-endA2-1)*2)
    else:
        a=answer
        answer=min(a+(midA-1)*2+len(name)-lastAidx-1,a+len(name)-(endA+1),a+Aidx+(len(name)-endA2-1)*2)
    return answer

print(solution(name))
