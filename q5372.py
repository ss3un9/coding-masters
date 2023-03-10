from itertools import product

N=int(input())

item=[1,2,3,4,5,6]

items=product(item, repeat=2)

for a,b in items:

    if int(a)+int(b)==N:
        print(a,b)



