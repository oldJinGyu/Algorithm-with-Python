a,b,c=map(int,input().split())
while a+b+c>0:
    if a+b+c<=max(a,b,c)*2:
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif a!=b and a!=c and b!=c:
        print('Scalene')
    else:
        print('Isosceles')
    a,b,c=map(int,input().split())