import sys
from sympy import isprime
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a=int(input())
    while True:
        if isprime(a):
            print(a)
            break
        else:
            a+=1