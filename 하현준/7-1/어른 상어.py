"""
https://www.acmicpc.net/problem/19237
"""
from collections import deque, defaultdict
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline


def smell_bye():
    for i in range(n):
        for j in range(n):
            if graph[i][j][1] > 0:
                graph[i][j][1] -= 1
                if graph[i][j][1] == 0:
                    graph[i][j][0] = 0


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
q = deque([[] for _ in range(m)])
graph = [[[0, 0] for _ in range(n)] for _ in range(n)]
priority = [[[] for _ in range(5)] for _ in range(m + 1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] != 0:
            graph[i][j][0] = data[j]
            graph[i][j][1] = k
            q[data[j] - 1] = [data[j], i, j]

direct = list(map(int, input().split()))
for idx, d in enumerate(direct):
    q[idx].append(d)

for i in range(m):
    for j in range(4):
        priority[i + 1][j + 1] = list(map(int, input().split()))

count = 0
while q:
    count += 1

    # 상어 이동
    check = defaultdict(list)
    for _ in range(len(q)):
        shark, sx, sy, sdirect = q.popleft()
        to_go = []
        for idx, p in enumerate(priority[shark][sdirect]):
            xx = sx + dx[p]
            yy = sy + dy[p]
            if not (0 <= xx < n and 0 <= yy < n):
                continue

            if graph[xx][yy][0] == 0:
                to_go.append([graph[xx][yy][0], idx, shark, xx, yy, p])
                break

            if graph[xx][yy][0] == shark:
                to_go.append([graph[xx][yy][0], idx, shark, xx, yy, p])
                continue

        if to_go:
            to_go.sort()
            _, _, tshark, txx, tyy, tp = to_go[0]
            check[(txx, tyy)].append([tshark, tp])
        else:
            check[(sx, sy)].append([shark, sdirect])

    # 냄새 사라지기
    smell_bye()

    # 이동 후 체크
    scount = 0
    who = 0
    for ck, cv in check.items():
        cxx, cyy = ck
        if len(cv) > 1:
            cv.sort()
        cshark, csdirect = cv[0]

        scount += 1
        who = cshark
        graph[cxx][cyy][0] = cshark
        graph[cxx][cyy][1] = k
        q.append([cshark, cxx, cyy, csdirect])

    if scount == 1 and who == 1:
        print(count)
        break

    if count >= 1000:
        print(-1)
        break

    print(count)
    print(q)
    print(*graph, sep="\n")
    print()
