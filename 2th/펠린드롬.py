import sys
input=sys.stdin.readline

def reverse(number):
    reverse_number=(str(number)[::-1])
    return int(reverse_number)

def finder(month):
    lst=[]
    month_day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range (1,month_day[month]+1):
        date=(month*100)+i
        reverse_date=reverse(date)
        
        if date==reverse_date:
            lst.append(date)
    return lst

day_lst=[]
target=0
a,b=map(int,input().split())
day=(a*100)+b

for i in range(1,13):
    day_lst.append(finder(i))

day_lst=sum(day_lst,[])

for date in day_lst:
    if day<date:
        target=date
        break
a=int(target/100)
b=int(target%100)

day=str(a)+' '+ str(b)
print(day)