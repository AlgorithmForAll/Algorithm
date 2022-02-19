"""
드래곤 커브
https://www.acmicpc.net/problem/15685
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def convert(x1, y1):
    if (x1, y1) == (1, 0):
        return (0, -1)
    if (x1, y1) == (0, -1):
        return (-1, 0)
    if (x1, y1) == (-1, 0):
        return (0, 1)
    if (x1, y1) == (0, 1):
        return (1, 0)


for _ in range(int(input())):
    answer = 0
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    graph = []
    for y, x, d, g in data:
        ex = x + dx[d]
        ey = y + dy[d]
        loc = deque([(ex, ey), (x, y)])
        for _ in range(g):
            rlist = []
            sx, sy = ex, ey
            for lx, ly in loc:
                converted = convert(lx - sx, ly - sy)
                sx, sy = lx, ly
                if converted is not None:
                    rlist.append(converted)
            for rx, ry in rlist:
                ex += rx
                ey += ry
                loc.appendleft((ex, ey))
        graph.extend(list(loc))
    graph = set(graph)
    for gx, gy in graph:
        if {(gx, gy + 1), (gx + 1, gy), (gx + 1, gy + 1)} <= graph:
            answer += 1
    print(answer)
