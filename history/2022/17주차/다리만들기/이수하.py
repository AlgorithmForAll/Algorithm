'''
bfs + dfs
거리저장 리스트 필요
'''
from collections import deque
from re import L
import sys


#섬찾기, 섬 카운팅
def bfsFindIsland(x, y):
    global count
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    graph[x][y] = count
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = count
                queue.append([nx, ny])

#섬과 섬을 잇는 다리의 최단거리 찾기
def bfsFindBridge(bridge):
    global bridgeCount
    queue = deque()
    
    # 거리저장할 리스트
    list = [[-1]*N for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == bridge:
                queue.append([i,j])
                list[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 갈 수 있는 곳이 없을 때
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 갈 수 있을 때
            if graph[nx][ny] == 0 and list[nx][ny] == -1:
                list[nx][ny] = list[x][y] + 1
                queue.append([nx, ny])
            # 다른 섬에 도달했을 때 전에 도달했던 값과 비교
            if graph[nx][ny] > 0 and graph[nx][ny] != bridge:
                bridgeCount = min(bridgeCount, list[x][y])
                return

N = int(input())

count = 1
bridgeCount = sys.maxsize

graph = [list(map(int, input().split()))  for i in range(N)]
visited = [[False]*N for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            bfsFindIsland(i, j)
            count += 1

for i in range(1, count):
    bfsFindBridge(i)

print(bridgeCount)