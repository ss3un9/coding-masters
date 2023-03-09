n = int(input())
words = []
for i in range(n):
    words.append(input())

# 중복 제거
unique_words = list(set(words))

# 길이에 따라 오름차순 정렬하고 같은 길이의 경우 알파벳순으로 정렬
sorted_words = sorted(unique_words, key=lambda x: (len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)