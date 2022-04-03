M, N = map(int, input().split())

Map = []
for i in range(M):
    tmp = list(map(int, input().split()))
    Map.append(tmp)

visited = [[0 for i in range(N)]for i in range(M)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]  # 상 상우 우 우하 하 하좌 좌 우상
dx = [0, 1, 1, 1, 0, -1, -1, -1]  # 상 상우 우 우하 하 하좌 좌 우상


def DFS(i, j):
    s = [[i, j]]
    while s:
        y, x = s.pop()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and visited[ny][nx] == 0 and Map[ny][nx] == 1:
                visited[ny][nx] = 1
                s.append([ny, nx])


count = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and Map[i][j] == 1:
            DFS(i, j)
            count += 1
print(count)
