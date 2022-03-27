"""
후위 표기식
https://www.acmicpc.net/problem/1918
"""
import sys
from collections import deque

sys.stdin = open("../input.txt")

priority = {
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 1
}

for _ in range(int(input())):
    result = []
    ostack = deque([])
    data = deque(list(input()))
    while data:
        now = data.popleft()
        if now.isalpha():  # 피연산자면 그대로 출력
            result.append(now)
        else:
            if now == ")":  # ) 이면 ( 가 나올 때까지 스택 pop
                while ostack:
                    o = ostack.pop()
                    if o == "(":
                        break
                    if o != ")":
                        result.append(o)
            elif now == "(":  # ( 이면 스택에 push
                ostack.append(now)
            else:  # 연산자면 스택에서 우선순위가 높거나 같은 것들 모두 pop
                while ostack:
                    o = ostack.pop()
                    if priority[o] < priority[now]:
                        ostack.append(o)
                        break
                    result.append(o)
                ostack.append(now)  # 그리고 현재 연산자를 스택에 push

    while ostack:  # 스택에 남은 연산자 모두 pop
        result.append(ostack.pop())

    print("".join(result))
