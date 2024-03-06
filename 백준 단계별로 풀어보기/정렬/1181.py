s=[]
for _ in range(int(input())):
    s.append(input())
s=set(s)
s=sorted(s,key=lambda x:(len(x),x))
for i in s:
    print(i)