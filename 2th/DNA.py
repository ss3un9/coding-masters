import sys
input=sys.stdin.readline

N=int(input())
lst=input()
lst=list(lst)
answer=[]
for i in range(0,N):
    if lst[i]=='A':
        answer.append('T')
    elif lst[i]=='T':
        answer.append('A')
    elif lst[i]=='G':
        answer.append('C')
    else:
        answer.append('G')
answer=''.join(answer)
print(answer)