##################쉬운 암호화#######################
# import math

# def test(n):
#     if n<2:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True

# def find(n):
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             j=n//i
#             if test(i) and test(j):
#                 print(i,j)
#                 return
#     print("IMPOSSIBLE")
    
# n=int(input())
# find(n)
#######################################################
# from itertools import combinations
# n,m=map(int,input().split())

# land=[list(map(int,input().split())) for _ in range(n)]

# max_sum=0

# for i in range(n-3):
#     for j in range(m-3):
#         sum=sum([land[i+x][j+y] for x in range(4) for y in range(4) if x+y!=3])
#         max_sum=max(max_sum,sum)

# print(max_sum)            
# for i in range(n):
#     for j in range(m):
#         if j+3<m:
#             sum_h=sum(land[i][j:j+4])
#             max_sum=max(max_sum,sum_h)
        
#         if i+3<n:
#             sum_v=sum(land[k][j] for k in range(i,i+4))
#             max_sum=max(max_sum,sum_v)
            
#         if i+3<n and j+3<m:
#             sum_d=sum(land[i+k][j+k] for k in range(4))
#             max_sum=max(max_sum,sum_d)
#         if i+3<n and j-3 <=0:
#             sum_r=sum(land[i+k][j-k] for k in range(4))
#             max_sum=max(max_sum,sum_r)


n,k=map(int,input().split())
stock=list(map(int,input().split()))

max_length=0
start=0
end=0
count=0
fail_day=0

for i in range(n):
    if stock[i]<stock[i-1]:
        fail_day+=1
        if fail_day>k:
            start+=1
            fail_day-=1
            
    end+=1
    if end - start>max_length:
        max_length=end-start
        answer_start=start+1
        answer_end=end
print(answer_start,answer_end)