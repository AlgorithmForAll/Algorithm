from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

# queue와 visited 2개 사용하기
visited_j = [[0] * m for _ in range(n)]
visited_f = [[0] * m for _ in range(n)]

queue_j = deque()
queue_f = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            queue_j.append([i, j])
            visited_j[i][j] = 1

        if graph[i][j] == 'F':
            queue_f.append([i, j])
            visited_f[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    # 1) 불 이동
    while queue_f:
        x, y = queue_f.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited_f[nx][ny] == 0 and graph[nx][ny] != '#':
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    queue_f.append([nx, ny])
    # 2) 지훈 이동
    while queue_j:
        x, y = queue_j.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited_j[nx][ny] == 0 and graph[nx][ny] != '#':
                    # 불이 퍼지지 않았거나, 불이 퍼지기전에 갈 수 있는 경우
                    if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        queue_j.append([nx, ny])
            else:
                return visited_j[x][y]
    return "IMPOSSIBLE"
print(bfs())
