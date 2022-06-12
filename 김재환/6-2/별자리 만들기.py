"""
MST,유니온파인드
"""
import heapq
import math

N = int(input())
stars = []
for n in range(N):
    x, y = map(float, input().split())
    stars.append([n, x, y])

q = []
for i in range(N):
    for j in range(i+1, N):
        # 길이 구하기;
        an, ax, ay = stars[i]
        bn, bx, by = stars[j]
        length = math.sqrt(abs(ay-by)**2 + abs(ax-bx)**2)
        heapq.heappush(q, [length, an, bn])


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


visited = [0 for i in range(N)]
parent = [i for i in range(N)]
answer = 0
while q:
    length, an, bn = heapq.heappop(q)
    if find(parent, an) != find(parent, bn):
        union(parent, an, bn)
        answer += length
        visited[an] = 1
        visited[bn] = 1
print("%.2f" % answer)
