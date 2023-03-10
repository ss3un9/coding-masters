
def case_1(n,arr):

    for i in range(n):
        flag = False  
        for j in range(n):
            
            if arr[i][j]==1:
                flag=True
                break
        
        if flag==False:
            for x in range(n):
                arr[i][x]=0
        
    return arr

def case_2(n,arr):
    for i in range(n):
        flag = False  
        for j in range(n):
            
            if arr[j][i]==1:
                flag=True
                break
        if flag==False:
            for x in range(n):
                arr[x][j]=0
        
    return arr
def main():
    n=int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]  

    count = 0  

    lst=arr.copy() 

    a=case_1(n,lst)

    result=case_2(n,a)
    for i in range(n):
        count+=arr[i].count(2)
        
    print(count)
    
if __name__ == '__main__':
    main()

