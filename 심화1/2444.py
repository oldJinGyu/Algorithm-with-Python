n=i=int(input())
for _ in range(2*i-1):
    n-=1
    print(" "*abs(n)+"*"*(2*(i-abs(n))-1))
