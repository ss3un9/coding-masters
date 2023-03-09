from queue import PriorityQueue

n = int(input()) # 편의점 개수
stations = [] # 편의점 정보를 저장할 리스트
for i in range(n):
    a, b = map(int, input().split())
    stations.append((a, b))
    
l, p = map(int, input().split()) # 식당까지 거리와 초기 포만감

# 편의점 정보를 거리순으로 정렬
stations.sort()

# bfs 알고리즘을 이용하여 편의점에 들르는 횟수를 계산
q = PriorityQueue()
q.put((-p, 0)) # 초기 상태를 큐에 추가
visited = [False] * n
ans = -1 # 만약 도착하지 못하는 경우 -1을 출력하기 위해 초기값을 -1로 설정
while not q.empty():
    food, cnt = q.get()
    food = -food # 우선순위 큐는 작은 값이 먼저 나오므로 -1을 곱해준 값으로 계산했던 포만감을 다시 되돌림
    if food >= l: # 식당에 도착했다면 반복문을 종료
        ans = cnt
        break
    for i in range(n):
        if not visited[i] and food >= stations[i][0]:
            visited[i] = True
            q.put((-(food - stations[i][0] + stations[i][1]), cnt+1))
            
print(ans)



