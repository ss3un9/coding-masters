n = int(input())

# pyramid 리스트 초기화
pyramid = [[[0] * (i+1) for j in range(i+1)] for i in range(n)]

# 1층 초기화
pyramid[0][0][0] = 1

# 2층부터 채우기
for i in range(1, n):
    for j in range(i+1):
        for k in range(i+1):
            if j == 0:  # 윗층 왼쪽 요소가 없을 때
                pyramid[i][j][k] = pyramid[i-1][j][k-1]
            elif k == 0:  # 윗층 위쪽 요소가 없을 때
                pyramid[i][j][k] = pyramid[i-1][j-1][k]
            else:
                pyramid[i][j][k] = pyramid[i-1][j-1][k] + pyramid[i-1][j][k-1]

# 출력
for i in range(n):
    for j in range(i+1):
        for k in range(i+1):
            print(pyramid[i][j][k], end=' ')
        print()