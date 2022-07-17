"""
https://www.acmicpc.net/problem/10971
pypy 통과, python 시간초과
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 5)


def travel(now, cost, count):
    global answer
    if count >= n:
        if w[now][start] != 0:
            answer = min(answer, cost + w[now][start])
        return

    for i in range(n):
        if w[now][i] != 0:
            if visited[i] == 0:
                visited[i] = 1
                travel(i, cost + w[now][i], count + 1)
                visited[i] = 0
    return

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

for start in range(n):
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    travel(start, 0, 1)

print(answer)
