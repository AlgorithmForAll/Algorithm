"""
3 2
1 3
2 3
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = {}
for i in range(1, N+1):
    adj[i] = []
counts = [0 for i in range(N+1)]
if N == 1:
    print(1)
    exit()
# 데이터를 갱신
for i in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    counts[B] += 1

q = deque([])
for i in range(1, N+1):
    if counts[i] == 0:
        q.append(i)
answer = []
while q:
    node = q.pop()
    answer.append(node)
    for child in adj[node]:
        if counts[child] == 1:
            q.append(child)
            counts[child] = 0
        else:
            counts[child] -= 1
print(" ".join(map(str, answer)))
