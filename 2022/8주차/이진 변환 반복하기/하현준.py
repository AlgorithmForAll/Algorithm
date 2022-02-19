"""
이진 변환 반복하기
https://programmers.co.kr/learn/courses/30/lessons/70129
"""
from collections import deque


def solution(s):
    zcount = 0
    rcount = 0
    q = deque(s)

    while True:
        qlen = len(q)
        rcount += 1
        while qlen:
            qlen -= 1
            n = q.popleft()
            if n == "0":
                zcount += 1
            else:
                q.append(n)
        if q == deque("1"):
            break

        q = deque(format(len(q), "0b"))

    return [rcount, zcount]


print(solution("110010101001"), [3, 8])
print(solution("01110"), [3, 3])
print(solution("1111111"), [4, 1])
