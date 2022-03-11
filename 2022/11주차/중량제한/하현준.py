"""
중량제한
https://www.acmicpc.net/problem/1939
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline
inf = float('inf')


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a


for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c, = map(int, input().split())
        edges.append((c, a, b))
        edges.append((c, b, a))

    n1, n2 = map(int, input().split())
    result = 0
    edges.sort(reverse=True)
    parent = [i for i in range(n + 1)]

    for weight, a, b in edges:
        if find_parent(parent, n1) != find_parent(parent, n2):
            union_parent(parent, a, b)
            result = weight

    print(result)
