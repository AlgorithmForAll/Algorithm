"""
분할 정복 스멜~~

"""
import sys
input = sys.stdin.readline

N = int(input())
Map = []
for n in range(N):
    tmp = list(map(int, input().split()))
    Map.append(tmp)


def isAll(Map, start, end):
    sy, sx = start
    ey, ex = end
    first = Map[sy][sx]
    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            if first != Map[i][j]:
                return False
    return True


dic = {-1: 0, 0: 0, 1: 0}


def recur(Map, N, start, end):
    first = Map[start[0]][start[1]]
    if N == 1:
        dic[first] += 1
        return
    if isAll(Map, start, end):
        dic[first] += 1
    else:
        sy, sx = start
        ey, ex = end
        for i in range(3):
            for j in range(3):
                _sy = sy + i * int(N/3)
                _sx = sx + j * int(N/3)
                _ey = _sy + int(N/3) - 1
                _ex = _sx + int(N/3) - 1
                recur(Map, N/3, [_sy, _sx], [_ey, _ex])


recur(Map, N, [0, 0], [N-1, N-1])


print(dic[-1])
print(dic[0])
print(dic[1])
