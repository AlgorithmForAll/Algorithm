"""
예상 대진표
https://programmers.co.kr/learn/courses/30/lessons/12985
"""


def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


def solution(n, a, b):
    count = 0
    while a != b:
        count += 1
        a = round2(a / 2)
        b = round2(b / 2)
    return count


print(solution(8, 4, 7), 3)

