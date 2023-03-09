import sys

N=input().strip()
lst=[]
for n in N:
    lst.append(n)

lst.reverse()

while True:
    if lst[0]=='0':
        lst.pop(0)
    else:
        break
    
        
result=0

for i in lst:
    result+=int(i)
    
print(''.join(lst))
print(result)