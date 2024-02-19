import sys
input=sys.stdin.readline

for _ in range(int(input())):
    r,n=map(int,input().split())
    
    nf=1
    for i in range(1,n+1):
        nf*=i
    nrf=1
    for i in range(1,n-r+1):
        nrf*=i
    rf=1
    for i in range(1,r+1):
        rf*=i
    print(nf//(nrf*rf))