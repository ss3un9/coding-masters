N,M=map(int,input().split())
cnt=0
while True:
    if N<M:
        N+=3
        cnt+=1
    elif N>M:
        N-=1
        cnt+=1
    else:
        break
print(cnt)