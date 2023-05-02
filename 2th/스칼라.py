import sys
input=sys.stdin.readline
N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

result=0
for i in range(0,N):
    result+=a[i]*b[i]
print(result)
    
