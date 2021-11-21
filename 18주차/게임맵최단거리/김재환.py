from collections import deque


def BFS(Map):

    r = len(Map)
    c = len(Map[0])

    visited = [[0 for i in range(c)] for i in range(r)]

    q = deque([[0, 0]])

    # 동서 남북
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    cnt = 1
    while q:
        cnt += 1
        for i in range(len(q)):
            y, x = q.popleft()
            if [y, x] == [r-1, c-1]:  # 도착지
                return cnt

            for _ in range(4):
                ny = y + dy[_]
                nx = x + dx[_]
                # 해당 범위, 방문 하지 않은 경우
                if (0 <= ny < r) and (0 <= nx < c) and visited[ny][nx] == 0 and Map[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1

    return -1


def solutions(maps):
    return BFS(maps)


solutions([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
          1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]	)
