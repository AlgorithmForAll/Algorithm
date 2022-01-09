"""
괄호 변환
https://programmers.co.kr/learn/courses/30/lessons/60058
"""


def divide(w):
    left, right = 0, 0
    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        elif w[i] == ")":
            right += 1
        if left * right > 0 and left == right:
            return w[:i+1], w[i+1:]


def check(u):
    if u[0] == ")":
        return False
    stack = []
    for i in range(len(u)):
        if u[i] == "(":
            stack.append("(")
        elif u[i] == ")":
            stack.pop()
        if not stack:
            return True
    return False


def solution(p):
    if len(p) == 0:
        return ""
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    return "(" + solution(v) + ")" + ''.join(['(' if x==')' else ')' for x in u[1:-1]])


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
