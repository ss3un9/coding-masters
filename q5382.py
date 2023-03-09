from collections import deque
N,M = map(int, input().split())
candy = list(map(int, input().split()))
cnt=0
candy_lst=[]
for i in range(N):
    candy_lst.append(i+1)
    
def left(target,lst):
    cnt=0
    deq = deque(lst)
    for i in range(len(deq)):
        if target==deq[0]:
            deq.popleft()
            return cnt,list(deq)
            break
        else:
            tmp=deq.popleft()
            deq.append(tmp)
            cnt+=1
def right(target,lst):
    cnt=0
    deq = deque(lst)
    for i in range(len(deq)):
        if target==deq[0]:
            deq.popleft()
            return cnt,list(deq)
            break
        else:
            tmp=deq.pop()
            deq.appendleft(tmp)
            cnt+=1                


for i in range(M):
    target=candy[i]
    left_cnt,left_lst=left(target,candy_lst)
    
    right_cnt,right_lst=right(target,candy_lst)
    
    if left_cnt>=right_cnt:
        cnt+=right_cnt
        candy_lst=right_lst
    else:
        cnt+=left_cnt
        candy_lst=left_lst

print(cnt)