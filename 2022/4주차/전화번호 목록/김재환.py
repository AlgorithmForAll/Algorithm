"""
sys.stdin.line으로 문자열을 받는경우
.strip()함수를 붙여서 공백과 newline을 지워줘야한다.
"""
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    numlist = []
    n = int(input())
    for i in range(n):
        tmp = input().strip()
        numlist.append(tmp)
    print(numlist)
    numlist.sort()
    print(numlist)
    print("----------------------")
    flag = 0
    for i in range(n-1):
        s = numlist[i]
        print("s:", s, " / next:", numlist[i+1])
        if len(s) <= len(numlist[i+1]) and s == numlist[i+1][:len(s)]:
            flag = 1
            break
        else:
            continue
    if flag == 0:
        print("YES")
    else:
        print("NO")
