"""
BFS
"""

from collections import deque
N, M = map(int, input().split())
Map = [0 for i in range(200)]
for n in range(N):
    a, b = map(int, input().split())
    Map[a] = b

for m in range(M):
    a, b = map(int, input().split())
    Map[a] = b


def BFS(Map):

    q = deque([1])
    count = 0
    visited = [0 for i in range(200)]
    visited[1] = 1
    while q:
        count += 1
        for _ in range(len(q)):
            p = q.popleft()

            if p >= 100:
                return count-1

            for i in range(p+1, p+1+6):
                if visited[i] == 0:
                    if Map[i] != 0:
                        q.append(Map[i])
                    else:
                        q.append(i)
                    visited[i] = 1


tmp = BFS(Map)
print(tmp)
