"""
안전거리 : 가장가까운 아기상어와의 거리
"""
from collections import deque

N, M = 0, 0


def BFS(shs):
    # 상 상우 우 하우 하 하좌 좌 상좌
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    visited = [[0 for i in range(M)] for i in range(N)]
    for sh in shs:
        visited[sh[0]][sh[1]] = 1

    count = 1
    q = deque(shs)
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()

            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = count
        count += 1

    answer = 0
    for v in visited:
        answer = max(answer, max(v))

    return answer


N, M = map(int, input().split())
Map = []
shs = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            shs.append([i, j])
    Map.append(tmp)
big = 0
big = max(big, BFS(shs))
print(big)
