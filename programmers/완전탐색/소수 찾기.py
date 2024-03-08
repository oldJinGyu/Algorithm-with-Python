import sys
from itertools import permutations
input=sys.stdin.readline

num=input().rstrip()

numbers = set()
for length in range(1, min(8, len(num)+1)):
    for perm in permutations(num, length):
        numbers.add(int(''.join(perm)))
nums=list(numbers)
n=max(nums)+1
lst=[True]*n
lst[0]=lst[1]=False
p=2
while p**2<=n:
    if lst[p] == True:
        for i in range(p**2,n,p):
            lst[i] = False
    p+=1
cnt=0
for i in nums:
    if lst[i]:
        cnt+=1
print(cnt)