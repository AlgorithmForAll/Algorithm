"""
MST + 조건부
서로 다른 노드끼리 이어져야한다.

"""
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


N, M = map(int, input().split())
gen = [0] + list(input().split())

hq = []
for m in range(M):
    u, v, d = map(int, input().split())

    heapq.heappush(hq, [d, u, v])

parent = [i for i in range(N+1)]

cost = 0
count = 0
while hq:
    d, u, v = heapq.heappop(hq)
    # 다른 성격의 대학교 + 다른 네트워크
    if gen[u] != gen[v] and find(parent, u) != find(parent, v):
        union(parent, u, v)
        cost += d
        count += 1
if count == N-1:
    print(cost)
else:
    print(-1)
