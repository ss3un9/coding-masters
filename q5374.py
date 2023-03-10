n,m=map(int,input().split())

if m>30:
    print(n,m-30)

else:
    if n!=0:
        print(n-1,m+30)
    else:
        print(23,m+30)