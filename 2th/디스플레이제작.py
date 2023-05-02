import sys
input=sys.stdin.readline
n = int(input())
min_diff = n  
result = (1, n) 


for i in range(1, n+1):
    if n % i == 0:
        a = i
        b = n // i
        if b>=a:
            diff = b - a
            if diff < min_diff:
                min_diff = diff
                result = (a, b)


print(result[0], result[1])