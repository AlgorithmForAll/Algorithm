import heapq
import sys
input = sys.stdin.readline


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, A, B):
    A = find(parent, A)
    B = find(parent, B)

    if A <= B:
        parent[B] = A
    else:
        parent[A] = B


P, W = map(int, input().split())
C, V = map(int, input().split())
hq = []
for w in range(W):
    s, e, w = map(int, input().split())
    heapq.heappush(hq, (-w, s, e))  # 최대힙으로 관리

parent = [i for i in range(P)]
total = []
while find(parent, C) != find(parent, V):
    w, s, e = heapq.heappop(hq)
    w = -w
    total.append(w)
    union(parent, s, e)
print(min(total))
