"""
mst + 유니온 파인드

"""
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
hq = []
for i in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(hq, [-C, A, B])  # 최대힙으로 사용
C1, C2 = map(int, input().split())


def union(parent, A, B):
    A = find(parent, A)
    B = find(parent, B)

    if A <= B:
        parent[B] = A
    else:
        parent[A] = B


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


answer = 1000000000
parent = [i for i in range(N+1)]
while hq:
    C, A, B = heapq.heappop(hq)
    C = -C
    union(parent, A, B)
    answer = min(answer, C)
    if find(parent, C1) == find(parent, C2):
        break
print(answer)
