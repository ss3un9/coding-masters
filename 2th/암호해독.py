import sys 
input=sys.stdin.readline
def find_len(N):
    result=0
    cnt=0
    for i in range(1,100):
        result+=i
        cnt+=1
        if result==N:
            break
    return cnt

def finder(text,N):

    lst=[text[0]]
    index=0
    for i in range(1,N):
        index+=i
        lst.append(text[index])
    return lst

text=input()
text=list(text)
N=len(text)-1
text_len=find_len(N)
answer=finder(text,text_len)
answer=''.join(answer)
print(answer)




