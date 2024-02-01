x = int(input())
n = int(input())
t = 0
for i in range(n):
    p, q = map(int, input().split())
    t += p*q
    
if t == x:
    print("Yes")
else:
    print("No")