N = int(input())
counts=[0]*10
for i in range(1,N+1):
    str_n=str(i)
    for j in str_n:
        counts[int(j)]+=1
        
print(*counts)