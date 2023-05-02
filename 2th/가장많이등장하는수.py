import sys
from collections import Counter
input=sys.stdin.readline

N=int(input())
lst=list(map(int,input().split()))
lst.sort()
count=Counter(lst)
a=(count.most_common(1))
print(a[0][0])