import re

T = int(input())
p = re.compile('(100+1+|01)+')
for i in range(T):
    tmp = input()
    if p.fullmatch(tmp) != None:
        print("YES")
    else:
        print("NO")
