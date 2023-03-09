'''
누적 합 트리란 각 원소가 2개씩 누적되어 합해지는 형태를 가진 트리를 의미합니다. 
승훈이는 이진 트리 자료구조를 공부하다가 누적 합을 가지는 이진 트리를 만들어보고 싶다는 생각을 했습니다. 
하지만 자료구조를 3번이나 재수강 했지만 모두 C+을 받은 승훈이는 스스로 이러한 프로그램을 작성할 능력이 없습니다.

그러므로 승훈이를 대신하여 주어진 원소로 누적 합 이진 트리를 만드는 프로그램을 작성해주세요.

입력값 설명

첫 번째 줄에는 원소의 갯수 N(1 ≤ N ≤ 4,095)이 주어집니다.
두 번째 줄에는 각 원소의 값 K(1 ≤ K ≤ 1,000)이 공백을 구분으로 주어집니다.

출력값 설명

누적 합을 가지는 이진 트리의 모든 원소를 최상단 원소부터 2의 거듭제곱 개수로 차례대로 출력합니다.
이 때 출력되는 이진 트리는 완전이진트리 형태입니다. 특정 위치의 원소가 없는 경우 그 값은 0이라고 간주합니다.

예제 입력1

6
1 9 3 8 4 5

예제 출력1

30
21 9
10 11 9 0
1 9 3 8 4 5 0 0

'''

import sys

def solution():
    N=int(input())
    arr=list(map(int,input().split()))
    if len(arr)==1:
        print(arr[0])
        
    else:
        
        for s in range(1, 15):
                if N <= 2**s:
                    break;   
        arr += [ 0 for _ in range(2**s - N) ]
        
        results=[arr]
    
        m=0
        
        while True:
            if len(results[m])//2==0:
                break
            else:
                results.append([])
                for i in range(0,len(results[m]),2):
                    results[m+1].append(results[m][i]+results[m][i+1])
                    
            
            m+=1
                    
        
        for result in results[::-1]:
            print(*result)
        
    
    
    


if __name__ == '__main__':
    solution()