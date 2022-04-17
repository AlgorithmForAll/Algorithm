"""
구간 합 구하기 5
https://www.acmicpc.net/problem/11660
"""
import sys

sys.stdin = open("../input.txt")

for _ in range(2):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())

    print(*graph, sep="\n")
    print()
    graph[1][1] += graph[0][0] + graph[0][1] + graph[1][0]
    for i in range(1, n):
        for j in range(1, n):
            if [i, j] != [1, 1]:
                graph[i][j] += graph[i][j - 1] + graph[i - 1][j]
    print(*graph, sep="\n")
    print("%")
