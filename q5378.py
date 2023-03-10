n = int(input())
num_list = list(map(int, input().split()))

# 모든 수를 더한 값이 3의 배수가 아니면 -1 출력
if sum(num_list) % 3 != 0 or 0 not in num_list:
    print(-1)
else:
    num_list.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans *= 10
        ans += num_list[i]
    if ans%300==0:
        
        print(ans)
    else:
        print(-1)
