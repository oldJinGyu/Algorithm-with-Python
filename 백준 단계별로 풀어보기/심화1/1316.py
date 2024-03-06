c=0
for _ in range(int(input())):
    s=input()
    e=0
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            a=s[i+1:]
            if a.count(s[i]):
                e+=1
    if e==0:
        c+=1
print(c)