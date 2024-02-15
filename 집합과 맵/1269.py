import sys
input=sys.stdin.readline
n=input()
print(len(list(set(map(int,input().split()))^set(map(int,input().split())))))