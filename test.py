'''from collections import deque
lst=[1,2,3,4,5]

deq=deque(lst)

a=deq.popleft()
deq.append(a)
'''
from collections import deque
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
    
a,b=(right(3,[2,3,4]))
print(a,b)

