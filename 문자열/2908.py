# x, y = input().split()
# x = x[::-1]
# y = y[::-1]
# x = int(''.join(x))
# y = int(''.join(y))
# print(max(x,y))
print(max(input()[::-1].split()))
#정수 비교에서 문자열로 비교해도 큰수가 아스키값이 더 크다.