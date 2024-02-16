import sys
input=sys.stdin.readline
n=int(input())
def check(n):
    if n==0 or n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for _ in range(n):
    a=int(input())
    while True:
        if check(a):
            print(a)
            break
        else:
            a+=1