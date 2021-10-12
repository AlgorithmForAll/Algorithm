
from itertools import product
case = [
    [],
    [0, 1, 2, 3],  # 1번 카메라의 경우의수
    [0, 1],  # 2번 카메라의 경우의 수
    [0, 1, 2, 3],  # 3번 카메라의 경우의 수
    [0, 1, 2, 3],  # 4번 카메라의 경우의 수
    [0]  # 5번 카메라의 경우의 수
]
N, M = map(int, input().split())
Map = []
cctv = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if 1 <= tmp[j] <= 5:
            cctv.append([tmp[j], i, j])
    Map.append(tmp)

# 경우의 수를 구하기
tmp = [case[i[0]] for i in cctv]
tmp = list(product(*tmp))


def fill(Map2, start, direction):  # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    Y, X = start
    for i in range(4):
        if direction[i] == 1:  # 출발~
            y, x = Y, X
            while True:
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= ny < N) and (0 <= nx < M) and Map2[ny][nx] != 6:
                    Map2[ny][nx] = '#'
                    y = ny
                    x = nx
                else:
                    break


small = N*M
for c in tmp:
    # 도화지 만들기
    Map2 = [[0 for i in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            Map2[i][j] = Map[i][j]
    # cctv 차례대로 값을 그려보기
    for z in range(len(cctv)):
        type, y, x = cctv[z]
        order = c[z]
        # type과 order의 방향에 따라 값을 칠한다.
        if type == 1:  # 4방향
            direction = [0, 0, 0, 0]
            direction[order] = 1
            fill(Map2, [y, x], direction)
        elif type == 2:
            if order == 0:
                fill(Map2, [y, x], [1, 1, 0, 0])
            else:
                fill(Map2, [y, x], [0, 0, 1, 1])
        elif type == 3:
            if order == 0:
                fill(Map2, [y, x], [1, 0, 0, 1])
            elif order == 1:
                fill(Map2, [y, x], [0, 1, 0, 1])
            elif order == 2:
                fill(Map2, [y, x], [0, 1, 1, 0])
            elif order == 3:
                fill(Map2, [y, x], [1, 0, 1, 0])
        elif type == 4:
            if order == 0:
                fill(Map2, [y, x], [1, 0, 1, 1])  # ㅗ
            elif order == 1:
                fill(Map2, [y, x], [1, 1, 0, 1])
            elif order == 2:
                fill(Map2, [y, x], [0, 1, 1, 1])
            elif order == 3:
                fill(Map2, [y, x], [1, 1, 1, 0])
        else:
            fill(Map2, [y, x], [1, 1, 1, 1])
    # 빈곳을 찾아본다.
    count = 0
    for i in range(N):
        for j in range(M):
            if Map2[i][j] == 0:
                count += 1
    small = min(small, count)
print(small)
