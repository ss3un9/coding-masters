def fibonacci():

    fib = [0] * (12)
    fib[1] = 1
    
    for i in range(2, 11):
        fib[i] = fib[i-1] + fib[i-2]

    return fib

a=fibonacci()
lst=[]
for i in range(1,len(a)):
    b=a[i]
    for j in range(b):
        lst.append(b)

a,b = map(int,input().split())
result=0
for i in range(a-1,b):
    result+=lst[i]
print(result)


    
