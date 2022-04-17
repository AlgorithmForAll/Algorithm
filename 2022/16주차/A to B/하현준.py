"""
A → B
https://www.acmicpc.net/problem/16953
"""
import sys

sys.stdin = open("../input.txt")


def dfs(x, count):
    global answer
    if x == b:
        answer = min(answer, count)
        return
    if x > b:
        return

    dfs(x * 2, count + 1)
    dfs(int(f"{x}1"), count + 1)


for _ in range(3):
    a, b = map(int, input().split())
    answer = float('inf')
    dfs(a, 0)
    print(answer + 1 if answer != float('inf') else -1)
