"""
줄 세우기
https://www.acmicpc.net/problem/2252
"""
from collections import deque

import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    indegree = [0 for _ in range(n + 1)]
    student = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b] += 1
        student[a].append(b)

    result = []
    q = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for node in student[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

    print(*result, sep=" ")