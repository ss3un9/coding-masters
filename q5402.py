import sys
def binary_search(arr, M):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == M:
            return mid
        elif arr[mid] < M:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

N,M=map(int,input().split())

arr=list(map(int,input().split()))

    
index=binary_search(arr, M)

if index==-1:
    print(-1)
else:
    print(index+1)


