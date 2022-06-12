import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n + 1)

edges = []
stars = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(n):
    a, b = map(float, input().split())
    stars.append((a, b))

for i in range(n - 1):
    for j in range(i + 1, n): 
        edges.append((math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost 

print(result)