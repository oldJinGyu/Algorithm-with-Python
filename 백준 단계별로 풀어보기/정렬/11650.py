l=[]
for _ in range(int(input())):
    [a,b]=map(int,input().split())
    l.append([a,b])
l.sort()
for i in l:
    print(*i)