n, m = map(int, input().split())  # 궁전의 크기 n, m 입력받기

castle = [list(map(int, input().split())) for _ in range(n)]  # 궁전의 상태 입력받기

count = 0  # 추가해야 하는 기둥의 개수를 저장하는 변수

for i in range(n):
    flag = False  # flag 변수를 사용하여 새로운 기둥을 추가할 지 여부를 판단
    for j in range(m):

        if castle[i][j]==0:
            flag=True
            break
    if flag==False:
        count+=1
        
        

          
print(count)  # 추가된 기둥의 개수 출력

