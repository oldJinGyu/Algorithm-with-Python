import sys
input=sys.stdin.readline

def kan(n):
    if n==0:
        return '-'
    kans=kan(n-1)
    l=[]
    for i in kans:
        l.append(i)
    for i in kans:
        l.append(' ')
    for i in kans:
        l.append(i)
    return l

while 1:
    try:
        n=int(input())
        print(''.join(kan(n)))
    except:
        break