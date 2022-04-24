"""
연구소 3
https://www.acmicpc.net/problem/17142
문제를 제대로 읽자 ㅄ아
"""

import sys
from itertools import combinations
from collections import deque

sys.stdin = open("../input.txt")
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def simulate():
    if blanks_len == 0:
        return 0
    max_val = -1
    count = 0
    q = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for vx, vy in case:
        visited[vx][vy] = 1
        graph[vx][vy] = 0
        q.append([vx, vy, 0])

    q = deque(q)
    while q:
        x, y, time = q.popleft()
        max_val = max(max_val, time)
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if visited[xx][yy] == 0 and graph[xx][yy] != "-":
                    if time + 1 >= answer:
                        return float('inf')

                    visited[xx][yy] = 1
                    if graph[xx][yy] != "*":
                        count += 1
                        if count == blanks_len:
                            return time + 1
                        graph[xx][yy] = time + 1
                        q.append([xx, yy, time + 1])
                    else:
                        q.append([xx, yy, time + 1])

    if count != blanks_len:
        return float('inf')

    return max_val


for _ in range(int(input())):
    answer = float('inf')
    n, m = map(int, input().split())
    graph = []
    vblocks = []
    blanks = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(n):
            if graph[i][j] == 2:
                vblocks.append([i, j])
                graph[i][j] = "*"
            elif graph[i][j] == 1:
                graph[i][j] = "-"
            else:
                blanks.append([i, j])

    blanks_len = len(blanks)
    for case in combinations(vblocks, m):
        val = simulate()
        answer = min(answer, val)
        # print(*graph,sep="\n")
        # print(val)
        for vx, vy in case:
            graph[vx][vy] = "*"
        for bx, by in blanks:
            graph[bx][by] = 0

    print(answer if answer != float('inf') else -1)
