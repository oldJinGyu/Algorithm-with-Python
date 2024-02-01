for _ in range(int(input())):
    a, s = input().split()
    print(''.join(j*int(a) for j in s))