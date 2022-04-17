from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    visited = [[0]*M for i in range(N)]
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                
                if shark[nx][ny] == 1:
                    return visited[nx][ny] - 1

N, M = map(int, input().split())
shark = [list(map(int, input().split())) for i in range(N)]

count = []
for i in range(N):
    for j in range(M):
        if shark[i][j] != 1:
            count.append(bfs(i, j))
        
print(max(count))