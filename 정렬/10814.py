l=[]
n=int(input())
for _ in range(n):
    a,b=input().split()
    l.append([int(a),b])
l=sorted(l,key=lambda x:x[0])
for i in l:
    print(int(i[0]),i[1])