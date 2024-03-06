a=int(input())
b=int(input())
c=int(input())

if (a+b+c)!=180:
    print('Error')
elif a!=b and a!=c and b!=c:
    print('Scalene')
elif a==b==c:
    print('Equilateral')
else:
    print('Isosceles')