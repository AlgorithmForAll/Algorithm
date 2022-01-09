"""
테트로미노
https://www.acmicpc.net/problem/14500
"""

import sys

input = sys.stdin.readline

result = 0
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
pieces = [
    [[1, 0, 0], [1, 0, 0], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 0], [0, 1, 0]],
    [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
    [[0, 1, 0], [0, 1, 0], [1, 1, 0]],
    [[0, 1, 0], [1, 1, 0], [1, 0, 0]],
    [[0, 1, 0], [1, 1, 1], [0, 0, 0]]
]

# 1x4
for i in range(n):
    for j in range(m - 3):
        result = max(result, sum(data[i][j:j + 4]))
data = list(map(list, zip(*data)))
for i in range(m):
    for j in range(n - 3):
        result = max(result, sum(data[i][j:j + 4]))
data = list(map(list, zip(*data)))

# 2x2
for i in range(n - 1):
    for j in range(m - 1):
        result = max(result, sum([data[i][j], data[i + 1][j], data[i][j + 1], data[i + 1][j + 1]]))

# 나머지 조각들
for i in range(-1, n):
    for j in range(-1, m):
        for p in range(6):  # 조각
            piece = pieces[p]
            for r in range(4):  # 회전
                temp = 0
                flag = False
                for x in range(3):
                    for y in range(3):
                        if piece[x][y] == 1:
                            try:
                                temp += data[i + x][j + y]
                            except IndexError:
                                flag = True
                                break
                    if flag:
                        break

                piece = list(map(list, zip(*piece[::-1])))  # 회전
                if not flag:
                    result = max(result, temp)

print(result)
