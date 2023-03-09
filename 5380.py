from math import factorial

A, B = map(int, input().split())

# A개의 원소에서 B개의 원소를 뽑는 조합에 대한 경우의 수 계산
comb = factorial(A) // (factorial(B) * factorial(A-B))

# 결과 출력
print(comb)