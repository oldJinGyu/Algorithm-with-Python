import sys
input=sys.stdin.readline

n=int(input())
def star(n):
    if n==1:
        return ['*']
    
    stars=star(n//3)
    l=[]
    print(stars)
    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+" "*(n//3)+s)
    for s in stars:
        l.append(s*3)
    return l
print('\n'.join(star(n)))