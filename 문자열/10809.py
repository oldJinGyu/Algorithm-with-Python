p = [-1]*26
s = map(str, input())
c = 0
for i in s:
    x = ord(i)-97
    if(p[x] == -1):
        p[x] = c
    c+=1
print(*p)
# print(*map(input().find, map(chr, range(97, 123))))