import sys
input=sys.stdin.readline

Q=int(input())
for _ in range(Q):
    Ta,Tb,Va,Vb=map(int,input().split())
    t=Tb*Vb+Ta*Va
    for i in range(Va+1):
        if Tb*Vb+Ta*(Va-i)>Ta*i:
            min=Tb*Vb+Ta*(Va-i)
        else:
            min=Ta*i
        if t>min:
            t=min
    print(t)