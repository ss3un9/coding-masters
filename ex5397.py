# -*- coding: utf-8 -*-
import sys

'''
@ 누적합(이진트리)
 -> 제일 아랫 줄의 숫자의 개수가 2^x
 -> 입력받은 수들의 자리 수가 부족하면 0으로 채워줘야 함
 -> 2층은 arr[0]+arr[1], arr[2]+arr[3], ...
 -> 3층도 ...

@ 야매 해법
 1. 제일 아랫 줄의 자리 수 계산
 2. 빈 만큼 0으로 채워 줌
 3. idx 0+1, idx 2+3, ... 반복하며 층을 쌓아올림(result에 저장)
    -> 새로 만든 층의 길이가 1인 경우, 이진트리를 완성한 것
 4. result에 저장한 값들을 출력 형식에 맞춰 출력함
'''

def solution():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    print(nums)
    # 첫 번째 줄 자리 수는 2^s 가 되어야 함
    #  -> 알맞은 s 찾기
    for s in range(1, 13):
        if n <= 2**s:
            break;

    # 입력이 1개인 경우 : 입력된 수 그대로 출력
    # -> 이 부분 필요한지는 잘 모르겠음
    # 암튼 넣음
    if len(nums) != 1:
        print(nums[0])
        
    # 입력이 2개 이상인 경우
    else:
        # 첫 번째 줄에 필요한 만큼 0으로 채워줌
        nums += [ 0 for _ in range(2**s - n) ]
        print(nums)
        # result : 출력할 결과들 저장하는 리스트
        results = [ nums ]
        r = 0   # 반복 횟수
        while True:
            # 반복 종료
            # -> 정점(= 노드의 길이가 1인 경우)까지 계산이 끝난 경우
            if len(results[r]) // 2 == 0:
                break;
            
            # 출력할 리스트를 계산?하는 부분
            results.append([])  # 새로운 리스트 추가
            # 새로운 리스트에 값을 채움
            for i in range(0, len(results[r]), 2):
                results[r+1].append(results[r][i] + results[r][i+1])
            r += 1
        
        # 계산한 결과들을 출력
        # *참고
        #  list -> [ [a, b], [c, d], [e, f] ]
        #  list[::-1] -> [ [e, f], [c, d], [a, b]]
        for result in results[::-1]:
            for r in result:
                print(f'{r}', end=' ')
            print()


if __name__ == '__main__':
    solution()