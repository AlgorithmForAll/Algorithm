"""
1로 테두리를 체크한 경우 겹치는 부분때문에 선과 면이 분리가 안되는 문제가 발생했다.
그래서 좌표를 전부 2배로 처리해주면 값이 커져서 분리가 명확해진다.
이후에 반으로 result를 나누어주면 된다.
"""
from collections import deque


def inSide(tmp, rec):
    lx, ly, rx, ry = rec  # 해당 좌표까지 먹기
    for i in range(ly, ry+1):
        if tmp[i][lx] != 2:
            tmp[i][lx] = 1
        if tmp[i][rx] != 2:
            tmp[i][rx] = 1
    for j in range(lx, rx+1):
        if tmp[ry][j] != 2:
            tmp[ry][j] = 1
        if tmp[ly][j] != 2:
            tmp[ly][j] = 1


def outSide(tmp, rec):
    lx, ly, rx, ry = rec  # 해당 좌표까지 먹기
    for i in range(ly+1, ry):
        for j in range(lx+1, rx):
            tmp[i][j] = 2


def BFS(tmp, start, end):  # return count

    dy = [-1, 1, 0, 0]  # 상하 좌우
    dx = [0, 0, -1, 1]
    sy, sx = start
    q = deque([[sy, sx, 0]])
    count = 1
    visited = [[0 for i in range(102)] for i in range(102)]
    visited[sy][sx] = 1
    while q:
        t = q.popleft()
        y, x, c = t
        if (y, x) == end:
            return c
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < 101) and (0 <= nx < 101) and tmp[ny][nx] == 1 and visited[ny][nx] != 1:
                q.append([ny, nx, c+1])
                visited[ny][nx] = 1


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    tmp = [[0 for i in range(102)] for i in range(102)]
    for rec in rectangle:
        lx, ly, rx, ry = rec  # 해당 좌표까지 먹기
        lx *= 2
        ly *= 2
        rx *= 2
        ry *= 2
        rec = [lx, ly, rx, ry]
        outSide(tmp, rec)
        inSide(tmp, rec)
    # BFS 길찾기
    answer = BFS(tmp, (characterY*2, characterX*2), (itemY*2, itemX*2))

    return answer//2
