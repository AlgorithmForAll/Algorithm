from collections import deque
from itertools import combinations
N, M = map(int, input().split())

virus = []
Map = []
empty = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            virus.append([i, j])
        if tmp[j] == 0:
            empty += 1
    Map.append(tmp)

cols = list(combinations(virus, M))


def BFS(Map, viruses):  # tuple

    # 상하 좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    _Map = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2 and [i, j] in viruses:
                _Map[i][j] = "*"
            else:
                _Map[i][j] = Map[i][j]

    q = deque([])
    visited = [[0 for i in range(N)] for i in range(N)]

    for v in viruses:
        y, x = v
        visited[y][x] = 1
        q.append([y, x, 0])

    time = 0
    num = 0
    while q:
        for _ in range(len(q)):
            y, x, c = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= ny < N) and (0 <= nx < N) and visited[ny][nx] == 0:
                    if _Map[ny][nx] == 0:
                        q.append([ny, nx, c+1])
                        visited[ny][nx] = 1
                        _Map[ny][nx] = 1
                        num += 1
                        time = max(time, c+1)
                    elif _Map[ny][nx] == "*":
                        _Map[ny][nx] = 1
                        visited[ny][nx] = 1
                        q.append([ny, nx, c])
    if num == empty:
        return time
    else:
        return -1


MAX = 100000000000
result = MAX
for col in cols:
    time = BFS(Map, col)
    if time != -1:  # 시간이 잘 나온경우
        result = min(result, time)
if result == MAX:
    print(-1)
else:
    print(result)
