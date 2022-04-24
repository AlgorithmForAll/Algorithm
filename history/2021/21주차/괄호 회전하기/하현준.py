"""
괄호 회전하기
https://programmers.co.kr/learn/courses/30/lessons/76502
"""
from collections import deque


def check(s):
    stack = deque([])
    for i in range(len(s)):
        if s[i] in ["(", "[", "{"]:
            stack.append(s[i])
        elif s[i] in [")", "]", "}"]:
            if stack:
                a = stack.pop()
                if s[i] == "}" and a == "{":
                    continue
                if s[i] == ")" and a == "(":
                    continue
                if s[i] == "]" and a == "[":
                    continue
            return False
    return len(stack) == 0


def solution(s):
    answer = 0
    n = len(s)
    q = deque(s)
    for i in range(n):
        if check(q):
            answer += 1
        q.append(q.popleft())

    return answer


print(solution("[](){}"), 3)
print(solution("}]()[{"), 2)
print(solution("[)(]"), 0)
print(solution("}}}"), 0)
