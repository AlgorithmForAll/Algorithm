"""
DSLR
https://www.acmicpc.net/problem/9019
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline


def operation(n, oper):
    if oper == 0:  # D
        n *= 2
        if n > 9999:
            n %= 10000
        return n, "D"
    if oper == 1:  # S
        if n == 0:
            return 9999, "S"
        n -= 1
        return n, "S"
    if oper == 2:  # L
        d1 = n // 1000
        d2 = (n % 1000) // 100
        d3 = (n % 100) // 10
        d4 = n % 10
        return int(f"{d2}{d3}{d4}{d1}"), "L"
    if oper == 3:  # R
        d1 = n // 1000
        d2 = (n % 1000) // 100
        d3 = (n % 100) // 10
        d4 = n % 10
        return int(f"{d4}{d1}{d2}{d3}"), "R"


result = []
for _ in range(int(input())):
    answer = ""
    A, B = map(int, input().split())
    visited = [0 for _ in range(10001)]
    q = deque([[A, ""]])
    visited[A] = 1
    while q:
        num, history = q.popleft()
        if num == B:
            answer = history if answer == "" else min(answer, history, key=len)
            print(answer)
            break

        for i in range(4):
            new_num, op = operation(num, i)
            if 0 <= new_num < 10000 and visited[new_num] == 0:
                visited[new_num] = 1
                q.append([new_num, history + op])
