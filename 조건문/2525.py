H, M = map(int, input().split())
T = int(input())

time = H*60+M+T

H = int((time/60)%24)
M = time%60

print(H,M)