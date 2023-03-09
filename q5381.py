n = int(input())
count = [0] * 10 # 0부터 9까지 숫자가 몇 번씩 나왔는지 저장하는 리스트

for i in range(1, n+1):
    for digit in str(i):
        count[int(digit)] += 1

print(*count)