import heapq

INF = int(1e9)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
distance = [[INF] * n for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상, 우, 하, 좌

# 다익스트라 알고리즘 구현
def dijkstra():
    q = []
    heapq.heappush(q, (grid[0][0], 0, 0))  # (거리, x, y)
    distance[0][0] = grid[0][0]  # 출발지의 떡의 수

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + grid[nx][ny]

                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

# 다익스트라 알고리즘 실행
dijkstra()


# 출발지에서 도착지까지 가는데 필요한 최소 떡의 수 출력
print(distance[n-1][n-1])
