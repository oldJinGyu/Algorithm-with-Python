list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
t = 0
for i in word:
    for j in list:
        for x in j:
            if i == x:
                t+=list.index(j)+3
print(t)