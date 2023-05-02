import sys
input=sys.stdin.readline

txt=input()
print(len(txt)-1)
split_txt=txt.replace(' ','')
print(len(split_txt)-1)

print(len(txt.split()))
