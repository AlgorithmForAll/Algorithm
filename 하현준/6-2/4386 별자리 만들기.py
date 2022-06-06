"""
https://www.acmicpc.net/problem/4386
"""
import heapq, math, sys

sys.stdin = open("../input.txt")
inf = float('inf')


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(10):
    n = int(input())
    location = [list(map(float, input().split())) for _ in range(n)]
    parent = [i for i in range(n + 1)]
    q = []
    result = 0
    for i in range(n):
        for j in range(i, n):
            ax, ay = location[i]
            bx, by = location[j]
            dist = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
            heapq.heappush(q, (dist, i, j))

    while q:
        dist, x, y = heapq.heappop(q)
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            result += dist
    print(f"{result:.3}")