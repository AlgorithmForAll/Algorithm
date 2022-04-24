"""
나만 안되는 연애
https://www.acmicpc.net/problem/14621
"""
import sys

sys.stdin = open("../../input.txt")


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


n, m = map(int, input().split())
univ = [''] + input().split()
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append([d, u, v])

cost = 0
edges.sort()
parent = [i for i in range(n + 1)]

for d, u, v in edges:
    if univ[u] != univ[v]:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            cost += d

for i in range(1, n + 1):
    parent[i] = find(parent, parent[i])

print(cost if len(set(parent[1:])) == 1 else -1)
