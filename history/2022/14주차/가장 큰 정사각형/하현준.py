"""
가장 큰 정사각형
https://www.acmicpc.net/problem/1915
"""
import sys

sys.stdin = open("../input.txt")
inf = float('inf')
for _ in range(int(input())):
    max_val = -inf
    n, m = map(int, input().split())
    graph = [list(map(int, input())) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        if graph[0][i] == 1 or graph[i][0] == 1:
            max_val = 1
            break

    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == 1:
                graph[i][j] = min(graph[i - 1][j] + 1, graph[i][j - 1] + 1, graph[i - 1][j - 1] + 1)
                max_val = max(max_val, graph[i][j])

    print(max_val ** 2 if max_val != -inf else 0)
