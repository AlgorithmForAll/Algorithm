import heapq

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x, y = 0, 0
count = 0

while True:
    v = int(graph[x][y])
    count += 1 

    q = []
    for i in range(4):
        nx = x + dx[i] * v
        ny = y + dy[i] * v
        if 0 <= nx < n and 0 <= ny < m:
            nv = graph[nx][ny]
            if nv == 'H':
                continue
            heapq.heappush(q, (int(nv), (nx, ny)))
    if q:
        nv, (nx, ny) = heapq.heappop(q)
        print(nv, (nx, ny))
        x, y = nx, ny            
    else:
        break
print(count)
# 실패: 길이 같은 경우를 고려하지 못함