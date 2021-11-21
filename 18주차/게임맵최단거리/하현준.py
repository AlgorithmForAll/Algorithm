"""
게임 맵 최단거리
https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
"""
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    answer = float('inf')
    n = len(maps)
    m = len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    q = deque([[0, 0, 1]])
    visited[0][0] = 1
    while q:
        x, y, count = q.popleft()
        if [x, y] == [n-1, m-1]:
            answer = min(answer, count)
            continue

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if maps[xx][yy] != 0 and visited[xx][yy] == -1:
                    visited[xx][yy] = 1
                    q.append([xx, yy, count + 1])
    return answer if answer != float('inf') else -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
