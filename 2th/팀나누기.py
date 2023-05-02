import sys
input=sys.stdin.readline
from itertools import permutations


lst=list(map(int,input().split()))
result=[]
for i in permutations(lst, 6):
    a=sum(i[:3])
    b=sum(i[3:])
    if a==b:
        print('possible')
        quit()
        
print('impossible')
    


    
# if a==b:
#     print('possible')
# else:
#     print('impossible')