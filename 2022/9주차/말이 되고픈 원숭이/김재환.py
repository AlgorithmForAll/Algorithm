"""
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
시작점과 도착점은 항상 평지
도착점까지 갈 수 없는 경우엔 -1을 출력

말처럼 뛰는 경우와 원숭이가되어 가는 경우 visited검증을 섬세하게 해야한다.
"""
from collections import deque

K = int(input())
W, H = map(int, input().split())
Map = []
for i in range(H):
    tmp = list(map(int, input().split()))
    Map.append(tmp)


def BFS():

    dy = [1, -1, 0, 0,  # 동서남북,
          -2, -1,  # 동북*2
          1, 2,  # 동남*2
          2, 1,  # 서남*2
          -1, -2]  # 서북*2 (시계방향)
    dx = [0, 0, -1, 1,
          1, 2,
          2, 1,
          -1, -2,
          -2, -1]
    visited = [[-1 for i in range(W)] for i in range(H)]
    visited[0][0] = K  # 이번엔 0부터 방문 했다는 뜻이다.

    q = deque([[0, 0, K]])
    move = -1
    while q:
        move += 1
        for i in range(len(q)):
            t = q.popleft()
            y, x, k = t
            if [y, x] == [H-1, W-1]:
                return move

            for i in range(12):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= ny < H) and (0 <= nx < W) and Map[ny][nx] == 0:
                    if 3 < i:  # 말처럼 뛰는 경우
                        if visited[ny][nx]+1 < k:
                            visited[ny][nx] = k-1
                            q.append([ny, nx, k-1])
                    elif i < 4:  # 걷는경우
                        if visited[ny][nx] < k:
                            visited[ny][nx] = k
                            q.append([ny, nx, k])
    return -1


print(BFS())
