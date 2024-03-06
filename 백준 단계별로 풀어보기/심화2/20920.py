import sys
input=sys.stdin.readline
n,m=map(int,input().split())
s={}
for _ in range(n):
    string=input().rstrip()
    if len(string)>=m:
        if string in s:
            s[string]+=1
        else:
            s[string]=1
s=sorted(s.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in s:
    print(i[0])