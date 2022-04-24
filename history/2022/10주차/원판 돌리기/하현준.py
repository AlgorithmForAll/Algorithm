"""
원판 돌리기
https://www.acmicpc.net/problem/17822
"""
import sys
from collections import deque

sys.stdin = open("../input.txt")
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    plates = [deque(list(map(int, input().split()))) for _ in range(n)]

    for _ in range(t):
        x, d, k = map(int, input().split())

        # rotate
        for p in range(1, n + 1):
            if p >= x and p % x == 0:
                if d == 0:
                    plates[p - 1].rotate(k)
                else:
                    plates[p - 1].rotate(-k)

        # find
        eliminate = []
        for i in range(n):
            for j in range(m):
                num = plates[i][j]
                if num != "x":
                    # j
                    for dy in [-1, 1]:
                        yy = j + dy
                        if yy >= m:
                            yy = 0
                        elif yy < 0:
                            yy = m - 1
                        if plates[i][yy] != "x" and num == plates[i][yy]:
                            eliminate.append([i, yy])

                    # i
                    for dx in [-1, 1]:
                        xx = i + dx
                        if 0 <= xx < n:
                            if plates[xx][j] != "x" and num == plates[xx][j]:
                                eliminate.append([xx, j])

        if eliminate:
            for ex, ey in eliminate:
                plates[ex][ey] = "x"
        else:
            avg = 0
            count = 0
            for i in range(n):
                for j in range(m):
                    num = plates[i][j]
                    if num != "x":
                        count += 1
                        avg += num

            if count > 0:
                avg /= count
                for i in range(n):
                    for j in range(m):
                        num = plates[i][j]
                        if num != "x":
                            if num > avg:
                                plates[i][j] -= 1
                            elif num < avg:
                                plates[i][j] += 1

    print(sum([sum([pp for pp in p if pp != "x"]) for p in plates]))
