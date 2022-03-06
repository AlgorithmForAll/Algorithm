"""
우선 리스트를 생성
제거하는 경우에는 DFS를 통해 확인한다.
"""
from collections import deque
N, M, T = map(int, input().split())
P = []
C = []
S = 0
NM = N*M
for i in range(N):
    tmp = deque(list(map(int, input().split())))
    S += sum(tmp)
    P.append(tmp)

for i in range(T):
    C.append(list(map(int, input().split())))


def DFS(visited, i, j, num):
    points = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = [[i, j]]
    visited[i][j] = 1
    points.append([i, j])
    while q:
        y, x = q.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0:
                nx = M-1
            else:
                nx = nx % M
            if (0 <= ny < N) and (0 <= nx < M) and visited[ny][nx] == 0 and P[ny][nx] == num:
                q.append([ny, nx])
                visited[ny][nx] = 1
                points.append([ny, nx])
    return points


for cmd in C:
    # 원판돌리기
    x, d, k = cmd
    for i in range(0, N):
        if (i+1) % x == 0:  # x의 배수들을 돌리기
            for _ in range(k):
                if d == 0:  # 시계방향
                    P[i].appendleft(P[i].pop())
                else:  # 반시계방향
                    P[i].append(P[i].popleft())
    visited = [[0 for i in range(M)] for i in range(N)]
    # 지울게 있는경우 BFS

    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and P[i][j] != 0:
                pointList = DFS(visited, i, j, P[i][j])
                if len(pointList) > 1:  # 지울게 있으면 제거한다.
                    for point in pointList:
                        count += 1
                        y, x = point
                        S -= P[y][x]
                        P[y][x] = 0
    NM -= count
    # 지운게 없는 경우
    if count == 0:
        if NM == 0:
            break
        avg = S/NM
        for i in range(N):
            for j in range(M):
                if P[i][j] != 0:
                    if P[i][j] == avg:
                        continue
                    elif P[i][j] < avg:
                        P[i][j] += 1
                        S += 1
                    else:
                        P[i][j] -= 1
                        S -= 1
print(S)
