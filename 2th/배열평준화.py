import sys
input=sys.stdin.readline


def finder(M):
    M.sort()
    return M[len(M)-1]-M[0]
N=int(input())
M=list(map(int,input().split()))

M.sort()
a = M[1:]
b = M[:-1] 
result1=finder(a)
result2=finder(b)

result=min(result1,result2)
print(result)
