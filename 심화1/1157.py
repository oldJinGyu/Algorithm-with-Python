a = input().upper()
b = list(set(a))
list = []
for i in b:
    list.append(a.count(i))
if list.count(max(list)) >= 2:
    print("?")
else: 
    print(b[list.index(max(list))])