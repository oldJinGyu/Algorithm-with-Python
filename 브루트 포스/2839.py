n=int(input())
for i in range(0,n//3+1):
    if (n-i*3)%5==0:
        print(int(i+(n-i*3)/5))
        break
else:
    print(-1)