import sys
input=sys.stdin.readline

answers=list(map(int,input().split()))

v1=[1,2,3,4,5]*(len(answers)//5+1)
v2=[2,1,2,3,2,4,2,5]*(len(answers)//8+1)
v3=[3,3,1,1,2,2,4,4,5,5]*(len(answers)//10+1)

answer=[]
cnt=[0,0,0]
for i in range(len(answers)):
    if answers[i]==v1[i]:
        cnt[0]+=1
    if answers[i]==v2[i]:
        cnt[1]+=1
    if answers[i]==v3[i]:
        cnt[2]+=1
max_cnt=max(cnt)
for i in range(3):
    if cnt[i]==max_cnt:
        answer.append(i+1)
print(answer)