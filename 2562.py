list = []
while True:
    try:
        list.append(int(input()))
    except:
        break
m = max(list)
print(m)
print(list.index(m)+1)