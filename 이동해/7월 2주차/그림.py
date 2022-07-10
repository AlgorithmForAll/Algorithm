from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited[x][y] = 1
    area = 1

    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    area += 1
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
    return area

count = 0
max_area = 0 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            area = bfs(i, j)
            # 그림의 개수
            count += 1
            # 가장 넓은 그림의 넓이
            max_area = max(area, max_area)

print(count)
print(max_area)