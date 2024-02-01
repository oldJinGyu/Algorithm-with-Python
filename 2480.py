d1, d2, d3 = map(int, input().split())

m = 0

if d1 == d2 and d2 == d3:
    m = 10000+d1*1000
elif d1 == d2 and d2 != d3:
    m = 1000+d1*100
elif d1 == d3 and d1 != d2:
    m = 1000+d1*100
elif d2 == d3 and d2 != d1:
    m = 1000+d2*100
else:
    m = max(d1, d2, d3)*100
    
print(m)