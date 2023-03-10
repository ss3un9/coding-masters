arr=[
    [0 ,1,0 ,1,0, 1, 0, 1],
    [1 ,0 ,1 ,0 ,1 ,0 ,1 ,0],
    [0 ,1 ,0 ,1 ,0 ,1 ,0 ,1],
    [1 ,0 ,1 ,0 ,1 ,0 ,1 ,0],
    [0 ,1 ,0 ,1 ,0 ,1 ,0 ,1],
    [1 ,0 ,1 ,0 ,1 ,0 ,1 ,0],
    [0 ,1 ,0 ,1 ,0 ,1 ,0 ,1],
    [1 ,0 ,1 ,0, 1 ,0, 1, 0]
    ]

str_arr=[list(map(str,input())) for _ in range(8)]
cnt=0
for i in range(8):
    for j in range(8):
        if str_arr[i][j] =='F' and arr[i][j]==0:
            cnt+=1
print(cnt)