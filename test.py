n = int(input())
sharks = list(map(int, input().split()))

kill_count = 1  # 연속해서 먹힐 수 있는 상어의 수
max_kill_count = 1  # 최대 연속해서 먹힐 수 있는 상어의 수
k=1
while k<n:
    
    
    for i in range(k, n):
        if sharks[i] >= sharks[i-1]:
            kill_count += 1
        else:
            max_kill_count = max(max_kill_count, kill_count)
            kill_count = 1
        #print(max_kill_count)
    k+=1

#max_kill_count = max(max_kill_count, kill_count)

print(max_kill_count)