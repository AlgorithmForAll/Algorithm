"""
치즈가 녹아 없어지는데 걸리는 시간()
녹기 한시간전 남아있는 치즈조각 개수(처음에 개수 세고 매번 제거하는 방식)

치즈 개수

공기 접촉 치즈 구하기=> 밖에서 DFS돌리면서 노출된 치즈 구하기
"""

R, C = map(int, input().split())
Map = []
count = 0
for i in range(R):
    tmp = list(map(int, input().split()))
    Map.append(tmp)
    count += sum(tmp)


def DFS():
    ch = set()
    dy = [-1, 1, 0, 0]  # 상하 좌우
    dx = [0, 0, -1, 1]
    start = [0, 0]
    visited = [[0 for i in range(C)]for i in range(R)]
    visited[0][0] = 1
    s = [start]
    while s:
        y, x = s.pop()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if (0 <= ny < R) and (0 <= nx < C):
                if Map[ny][nx] == 0 and visited[ny][nx] == 0:
                    s.append([ny, nx])
                    visited[ny][nx] = 1
                elif Map[ny][nx] == 1:  # 치즈인경우
                    ch.add((ny, nx))
    return ch


time = 0
_count = count
while True:
    ch = DFS()
    if len(ch) == 0:
        break

    chNum = len(ch)
    for c in ch:
        y, x = c
        Map[y][x] = 0  # 치즈 제거

    _count = count
    count -= chNum
    time += 1

print(time)
print(_count)
