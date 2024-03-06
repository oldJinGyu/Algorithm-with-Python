n=int(input())
for i in range(int(10**(len(str(n))-2)),n):
    s=sum(map(int,str(i)))
    t=i+s
    if n==t:
        print(i)
        break
else:
    print(0)