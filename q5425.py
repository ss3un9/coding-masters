'''민규는 가벼운 기억상실증을 앓고 있습니다. 
오늘 무엇인가를 외우면 잠을 자면서 일부를 잊는 증세를 보입니다. 영어시험을 준비하는 민규는 단어 N개를 모두 외워야 합니다.
민규는 하루에 A개의 단어를 외울 수 있습니다. 하지만, 밤에 잠을 자면서 B개를 까먹습니다. N개를 모두 외우는 날에 민규는 목적을 달성합니다.



또한 모두 외우는 날에는 밤에 단어를 까먹는 것을 생각하지 않고 N개의 단어를 모두 외웠다고 간주합니다. 
민규가 외워야 하는 N개의 단어가 주어졌을 때, 단어를 모두 외우려면 며칠이 걸리는지 구하는 프로그램을 작성해주세요'''

import sys

a,b,answer=map(int, input().split())
remember=0
cnt=0
while True:
    cnt+=1
    remember+=a
    
    if remember<answer:
        remember-=b

    else:
        break
print(cnt)
        