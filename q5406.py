import sys
N=int(input())
arr = [[0]*N for i in range(N)]

'''
0,0 1,0 2,0
0,1 1,1 2,1
0,2 1,2 2,2
'''
count=1

for i in range(N):
    for j in range(N):
        arr[j][i]=count
        count+=1

        
for i in arr:
    print(*i)