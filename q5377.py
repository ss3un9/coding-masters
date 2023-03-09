N = int(input())  # 찾을 숫자 N 입력받기

count = 0  # N이 포함된 시간의 개수를 저장할 변수 초기화

# 시, 분, 초에 대해 0부터 59까지 반복하면서 N이 포함되어 있는지 확인
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            time_str = f'{hour:02d}:{minute:02d}:{second:02d}'  # 시간을 문자열로 표현
            if str(N) in time_str:  # N이 포함되어 있는지 확인
                count += 1

print(count)  # N이 포함된 시간의 개수 출력