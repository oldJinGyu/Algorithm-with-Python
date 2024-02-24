import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
if len(nums)==1:
    if 1 in nums:
        print("NO")
    else:
        print('YES')
        print(nums[0]*10+nums[0])
elif len(nums)==2:
        if 0 in nums and 1 in nums:
            print('YES')
            print(0)
        else:
            print('YES')
            print(nums[1]*10+nums[1])
else:
    print('YES')
    print(nums[2]*10+nums[2])