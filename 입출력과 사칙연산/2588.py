a = int(input())
b = int(input())

print(int(b%10*a))
print(int(((b%100)-b%10)/10*a))
print(int((b - b%100)/100*a))
print(a*b)