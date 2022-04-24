"""
https://www.acmicpc.net/problem/2447
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 5)


def dfs(x, y, gsize):
    if gsize == 1:
        return

    sx, sy = gsize // 3, gsize // 3
    for i in range(x + sx, x + sx * 2):
        for j in range(y + sy, y + sy * 2):
            graph[i][j] = " "

    for i in range(x, x + sx * 2 + 1, sx):
        for j in range(y, y + sy * 2 + 1, sx):
            if [i, j] != [x + sx, y + sy]:
                dfs(i, j, gsize // 3)


for k in range(1, 9):
    n = int(input())
    graph = [["*" for _ in range(n)] for _ in range(n)]
    dfs(0, 0, n)
    for g in graph:
        print("".join(g))
