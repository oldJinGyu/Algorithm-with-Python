import sys
input=sys.stdin.readline
nums=[]
for _ in range(int(input())):
    nums.append(int(input()))
nums.sort()
print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])
num={};l=[]
for i in nums:
    if i in num:
        num[i]+=1
    else:
        num[i]
mx=max(num.values())
for i in num:
    if num[i]==mx:
        l.append(i)
if len(l)==1:
    print(l[0])
else:
    print(l[1])
print(max(nums)-min(nums))