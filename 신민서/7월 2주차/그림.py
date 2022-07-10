def bfs(ii, jj, n, m):
    arr[i][j] = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = [[i, j]]
    count = 0
    while q:
        x, y = q.pop(0)
        count += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append([nx, ny])
                    arr[nx][ny] = -1
    return count

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

largest, cnt = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            largest = max(bfs(i, j, n, m), largest)
            cnt += 1

print(cnt, largest)