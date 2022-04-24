"""
반례
북서동남으로 찾아도 안된다. 반례 존재함.
0 0 0 0 0 0
0 0 0 0 0 p
p 0 0 t 0 0
0 0 0 0 0 0
0 0 0 0 0 0
인 경우 오른족 위가 맞음에도 불구하고
왼쪽에 있는 p를 큐에서 먼저 접근하기 때문에 반례가 존재한다.
"""
from collections import deque
N, M, F = map(int, input().split())

Map = []
for i in range(N):
    tmp = list(map(int, input().split()))
    Map.append(tmp)
ty, tx = map(int, input().split())
passengers = {}
for i in range(M):
    sy, sx, dy, dx = map(int, input().split())
    passengers[(sy-1, sx-1)] = (dy-1, dx-1)
    Map[sy-1][sx-1] = 2


def findPassengers(start):
    dy = [-1, 0, 0, 1]  # 북 서 동 남
    dx = [0, -1, 1, 0]  # 북 서 동 남
    y, x = start
    q = deque([[y, x, 0]])
    visited = [[0 for i in range(N)]for i in range(N)]
    visited[y][x] = 1
    f = (-1, -1, -1)
    while q:
        _q = list(q)
        for i in range(len(q)):
            y, x, c = q.popleft()
            if Map[y][x] == 2:
                f = (y, x, c)
                break
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= ny < N) and (0 <= nx < N) and Map[ny][nx] != 1 and visited[ny][nx] != 1:
                    q.append([ny, nx, c+1])
                    visited[ny][nx] = 1
        if f != (-1, -1, -1):
            break
    if f == (-1, -1, -1):  # 못찾은 경우
        return f
    else:
        _q.sort()
        for dot in _q:
            y, x, c = dot
            if Map[y][x] == 2:
                Map[y][x] = 0
                return dot


def findDestination(start, destination):
    dy = [-1, 0, 0, 1]  # 북 서 동 남
    dx = [0, -1, 1, 0]  # 북 서 동 남
    y, x = start
    q = deque([[y, x, 0]])
    visited = [[0 for i in range(N)]for i in range(N)]
    visited[y][x] = 1
    f = (-1, -1, -1)
    while q:
        y, x, c = q.popleft()
        if (y, x) == destination:
            f = (y, x, c)
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < N) and (0 <= nx < N) and Map[ny][nx] != 1 and visited[ny][nx] != 1:
                q.append([ny, nx, c+1])
                visited[ny][nx] = 1
    return f


cost = F
ty, tx = ty-1, tx-1
for i in range(len(passengers)):
    # 승객 찾기
    pstart = findPassengers((ty, tx))
    if pstart == (-1, -1, -1):  # 승객을 찾을 수 없는경우
        print(-1)
        exit(0)
    sy, sx, sc = pstart  # 현재 -> 승객의 위치, 비용

    pend = findDestination((sy, sx), passengers[(sy, sx)])
    if pend == (-1, -1, -1):  # 승객을 찾을 수 없는경우
        print(-1)
        exit(0)

    fy, fx, fc = pend  # 승객 -> 목적지위치, 비용

    print("현재 연료:", cost)
    print("지금:", [ty, tx], "  승객:", [sy, sx, sc], "  목적지:", [fy, fx, fc])
    # 손님 태우러 가는길
    cost -= sc
    # 목적지 가는길
    cost -= fc
    if cost >= 0:
        cost += fc*2
        ty = fy
        tx = fx
    else:
        # 연료가 감당이 안되는 경우
        print(-1)
        exit(0)
    #print("최종연료:", cost)
print(cost)
