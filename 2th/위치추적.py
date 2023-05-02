import sys
input=sys.stdin.readline

n = int(input())  
x, y = 0, 0  

for i in range(n):
    x1, y1 = map(int, input().split())
    if x1 == 1:
        x += y1
    elif x1 == 2:
        y += y1
    elif x1 == 3:
        x -= y1
    else:
        y -= y1

print(x, y)