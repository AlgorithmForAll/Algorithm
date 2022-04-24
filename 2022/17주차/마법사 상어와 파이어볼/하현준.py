"""
마법사 상어와 파이어볼
https://www.acmicpc.net/problem/20056
"""
import sys

sys.stdin = open("../input.txt")
from collections import deque, defaultdict

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def check(data):
    even = 0
    odd = 0
    for d in data:
        if d % 2 == 0:
            even += 1
        elif d % 2 == 1:
            odd += 1
    return even * odd == 0


for _ in range(6):
    n, m, k = map(int, input().split())
    fire_ball = deque([])
    for _ in range(m):
        r, c, m, s, d = list(map(int, input().split()))
        fire_ball.append([r - 1, c - 1, m, s, d])

    for _ in range(k):
        data = defaultdict(list)
        while fire_ball:
            for _ in range(len(fire_ball)):
                r, c, m, s, d = fire_ball.popleft()
                r = (r + dx[d] * s) % n
                c = (c + dy[d] * s) % n
                data[(r, c)].append([m, s, d])

        for dk, dv in data.items():
            dr, dc = dk
            if len(dv) > 1:
                total_m, total_s, total_d = list(map(list, zip(*dv)))
                div_m = int(sum(total_m) / 5)
                if div_m > 0:
                    div_s = int(sum(total_s) / len(dv))
                    if check(total_d):
                        for dd in [0, 2, 4, 6]:
                            fire_ball.append([dr, dc, div_m, div_s, dd])
                    else:
                        for dd in [1, 3, 5, 7]:
                            fire_ball.append([dr, dc, div_m, div_s, dd])
            else:
                fire_ball.append([dr, dc, dv[0][0], dv[0][1], dv[0][2]])

    answer = 0
    for i in range(len(fire_ball)):
        answer += fire_ball[i][2]
    print(answer)
