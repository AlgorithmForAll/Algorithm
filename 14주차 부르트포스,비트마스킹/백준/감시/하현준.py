"""
감시
https://www.acmicpc.net/problem/15683
"""
from collections import defaultdict
from itertools import product

direction = [
    [],
    [[[0, 1]], [[0, -1]], [[1, 0]], [[-1, 0]]],
    [[[0, 1], [0, -1]], [[-1, 0], [1, 0]]],
    [[[-1, 0], [0, 1]], [[-1, 0], [0, -1]], [[0, -1], [1, 0]], [[1, 0], [0, 1]]],
    [[[0, 1], [0, -1], [1, 0]], [[0, 1], [0, -1], [-1, 0]], [[0, 1], [1, 0], [-1, 0]], [[0, -1], [1, 0], [-1, 0]]],
    [[[0, 1], [0, -1], [1, 0], [-1, 0]]]
]
n, m = map(int, input().split())
cctv = defaultdict(list)
graph = []
cases = []
answer = 65
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 0 < graph[i][j] < 6:
            cctv[graph[i][j]].append([i, j])

limit = -1
for k, v in cctv.items():
    if k in [1, 3, 4]:
        limit = 4
    elif k == 2:
        limit = 2
    elif k == 5:
        limit = 1
    temp = list(product(v, [i for i in range(limit)]))
    for i in range(0, len(temp), limit):
        cases.append(temp[i:i + limit])

cases = list(product(*cases))

for case in cases:
    for i in range(len(case)):
        loc, dtype = case[i]
        x, y = loc
        ctype = graph[x][y]
        for d in range(len(direction[ctype][dtype])):  # 감시 시작
            xx, yy = x, y
            while True:
                xx += direction[ctype][dtype][d][0]
                yy += direction[ctype][dtype][d][1]
                if 0 <= xx < n and 0 <= yy < m:
                    if graph[xx][yy] == 6:
                        break
                    if 1 <= graph[xx][yy] <= 5:
                        continue
                    graph[xx][yy] = -1
                else:
                    break

    count = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 0:
                count += 1
            elif graph[a][b] == -1:
                graph[a][b] = 0
    answer = min(answer, count)

print(answer)
