from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dw = [1, -1]
q = deque([])

def bfs(arr):
    global answer, m, n, h
    while q:
        cursize = len(q)
        for c in range(cursize):
            w, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[w][nx][ny] == 0:
                        arr[w][nx][ny] = 1
                        q.append([w, nx, ny])
            for i in range(2):
                nw = w + dw[i]
                if 0 <= nw < h:
                    if arr[nw][x][y] == 0:
                        arr[nw][x][y] = 1
                        q.append([nw, x, y])
        answer += 1


global answer, m, n, h
m, n, h = map(int, input().split())
arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
answer = 0
allofthem = True

for hh in range(h):
    for i in range(n):
        adding = list(map(int, input().split()))
        for j in range(m):
            arr[hh][i][j] = adding[j]
            if adding[j] == 0:
                 allofthem = False

if allofthem == True:
    print(0)
    exit()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                q.append([k, i, j])
cnt = 0
if not q:
    answer = -1
else:
    bfs(arr)
    allofthem = True
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 0:
                    allofthem = False

if allofthem == False:
    answer = -1
else:
    answer -= 1
print(answer)



