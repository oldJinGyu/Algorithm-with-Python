import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
op=list(map(int,input().split()))
opl=['+']*op[0]+['-']*op[1]+['*']*op[2]+['/']*op[3]
kings=permutations(opl)
rs=[]
for i in kings:
    num=nums[0]
    for j in range(n-1):
        if i[j]=='+':
            num+=nums[j+1]
        elif i[j]=='-':
            num-=nums[j+1]
        elif i[j]=='*':
            num*=nums[j+1]
        elif i[j]=='/':
            if num<0:
                num=-(-num//nums[j+1])
            else:
                num//=nums[j+1]
    rs.append(num)
print(max(rs))
print(min(rs))