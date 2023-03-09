import sys
import math
N,M=map(int,input().split())
coins=[]
cnt=0
for i in range(N):
    num=int(input())
    coins.append(num)

coins.sort(reverse=True)

for coin in coins:
    if M>0:
        cnt+=M/coin
        cnt=math.trunc(cnt)
        M%=coin
        
    else:
        break
    
if M==0:
    print(cnt)
else:
    print(-1)
        
