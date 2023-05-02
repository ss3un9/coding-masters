import sys
input=sys.stdin.readline


def randoms(X,A,B,C):
    return ((X*A)+B)%C

X,A,B,C,N=map(int,input().split())

for i in range(N):
    X=randoms(X,A,B,C)
print(X)
