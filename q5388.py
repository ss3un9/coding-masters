n = int(input())
dp = [[0] * (i + 1) for i in range(n)]

# 첫 번째 산 정상에 놓인 동전의 개수를 dp[0][0]에 저장
dp[0][0] = int(input())

# 산에서 내려오면서 dp 테이블 채우기
for i in range(1, n):
    row = list(map(int, input().split()))
    # 첫 번째 열
    dp[i][0] = dp[i-1][0] + row[0]
    # 중간 열들
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + row[j]
    # 마지막 열
    dp[i][i] = dp[i-1][i-1] + row[i]

# dp 배열에서 최대값 찾기
answer = max(dp[n-1])
print(answer)

