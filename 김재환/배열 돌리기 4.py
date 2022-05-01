"""
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
시계방향으로만 회전
"""
from itertools import permutations


def spin(_Map, r, c, s):
    sy, sx = r-s-1, c-s-1
    ey, ex = r+s-1, c+s-1

    for _ in range(int((ey-sy)//2)):
        tmp = _Map[sy][sx]
        for i in range(ey-sy):  # 왼쪽
            _Map[sy+i][sx] = _Map[sy+1+i][sx]
        for i in range(ex-sx):  # 아래
            _Map[ey][sx+i] = _Map[ey][sx+1+i]
        for i in range(ey-sy):  # 오른쪽
            _Map[ey-i][ex] = _Map[ey-1-i][ex]
        for i in range(ex-sx):  # 위
            _Map[sy][ex-i] = _Map[sy][ex-1-i]

        _Map[sy][sx+1] = tmp
        sy, sx = sy+1, sx+1
        ey, ex = ey-1, ex-1


Map = []
N, M, K = map(int, input().split())
for n in range(N):
    Map.append(list(map(int, input().split())))
cases = []
for k in range(K):
    cases.append(list(map(int, input().split())))

answer = 100 * M
# 케이스 구하기
for pers in list(permutations(cases, len(cases))):
    _Map = [[0 for i in range(M)] for i in range(N)]
    for y in range(N):
        for x in range(M):
            _Map[y][x] = Map[y][x]
    for per in pers:
        spin(_Map, *per)
    # 최솟값 구하기
    small = 100 * M
    for n in range(N):
        small = min(small, sum(_Map[n]))
    answer = min(answer, small)
print(answer)
