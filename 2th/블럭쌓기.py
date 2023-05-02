def count_tower_sequences(n, k):
    def build_tower(height, blocks, seq):
        nonlocal count
        if height == k:
            count += 1
            return
        for i in range(1, n + 1):
            if height == 0 or i > seq[height - 1]:
                if blocks >= i:
                    seq[height] = i
                    build_tower(height + 1, blocks - i, seq)
                    seq[height] = 0
    
    count = 0
    blocks = n * (n + 1) // 2 - k * (k - 1) // 2
    build_tower(0, blocks, [0] * k)
    return count

# 입력 예시
n = 6
k = 3

# 서로 다른 수열의 개수를 출력
print(count_tower_sequences(n, k))
