a,b,v=map(int, input().split())
# if (v-a)/(a-b)>(v-a)//(a-b):
#     if (v-a)//(a-b)*(a-b)+a < v:
#         print((v-a)//(a-b)+2)
#     else:
#         print((v-a)//(a-b)+1)
# else:
#     print(int((v-a)/(a-b))+1)
d=(v-b)/(a-b)
print(int(d) if d==int(d) else int(d)+1)