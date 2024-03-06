n = int(input())
list = list(map(int, input().split()))
m = max(list)
print(sum(list)/m*100/n)