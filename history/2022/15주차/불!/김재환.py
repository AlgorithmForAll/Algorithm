"""
BFS로 하면 될듯?
불이 여러군데일수도 있음
불에 타기전에 탈출해야함 -> 지훈이가 존재하는 위치에서 불에 타버리면 제거해야함.
"""
from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
Map = []
F = []
for r in range(R):
    tmp = list(input())
    for c in range(C):
        if tmp[c] == 'J':
            J = [r, c, 'J']
        elif tmp[c] == 'F':
            F.append([r, c, 'F'])
    Map.append(tmp)


def BFS(J, F):

    dy = [-1, 1, 0, 0]  # 상하 좌우
    dx = [0, 0, -1, 1]

    visited = [[0 for i in range(C)] for i in range(R)]
    q = deque([J]+F)
    count = -1
    while q:
        count += 1
        for _ in range(len(q)):
            y, x, c = q.popleft()

            if c == 'J' and Map[y][x] == 'F':  # 불에 타버린 지훈이
                continue
            if c == 'J' and (y == 0 or y == R-1 or x == 0 or x == C-1):  # 마지막에 도달
                return count+1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 벽이 아니어야한다.
                if (0 <= ny < R) and (0 <= nx < C) and Map[ny][nx] != '#':
                    if c == 'J' and Map[ny][nx] == '.' and visited[ny][nx] == 0:
                        q.append([ny, nx, c])
                        visited[ny][nx] = 1
                    elif c == 'F' and Map[ny][nx] != 'F':
                        q.append([ny, nx, c])
                        Map[ny][nx] = 'F'
    return "IMPOSSIBLE"


tmp = BFS(J, F)
print(tmp)
