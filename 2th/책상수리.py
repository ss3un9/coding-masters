import sys
input=sys.stdin.readline

N,K=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

for s in a:
    if K<=s:
        print(s)
        break
    