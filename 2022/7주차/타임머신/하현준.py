"""
타임머신
https://www.acmicpc.net/problem/11657
다익스트라 알고리즘은 음의 가증치를 가지는 간선이 있는 경우 최단 거리를 구할 수 없다.
"""

import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline
INF = float('inf')


def bellman():
    dist[1] = 0

    for _ in range(n - 1):
        for a, b, c in graph:
            if dist[a] != INF and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c

    for a, b, c in graph:
        if dist[a] != INF and dist[a] + c < dist[b]:
            return False

    return True


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    dist = [INF for _ in range(n + 1)]
    if not bellman():
        print(-1)
    else:
        for d in dist[2:]:
            print(d if d != INF else -1)

