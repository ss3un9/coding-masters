import sys

N=(input().split())
M=(input().split())

for i in range(len(M)):
    if N[1]==M[i]:
        print(i+1)
