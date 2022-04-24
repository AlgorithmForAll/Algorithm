"""
최종목표: 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수
좌표로 진행하면 안되는 문제가 있었는데 까먹었음.....
"""


from collections import deque


N = int(input())


def roll(endpoint, q):
    for i in range(len(q)-1, -1, -1):
        y, x, d = q[i]
        if d == 0:
            _d = 1
            q.append((endpoint[0], endpoint[1], _d))
            endpoint[0] -= 1
        elif d == 1:
            _d = 2
            q.append((endpoint[0], endpoint[1], _d))
            endpoint[1] -= 1
        elif d == 2:
            _d = 3
            q.append((endpoint[0], endpoint[1], _d))
            endpoint[0] += 1
        elif d == 3:
            _d = 0
            q.append((endpoint[0], endpoint[1], _d))
            endpoint[1] += 1


Map = [[0 for i in range(101)] for i in range(101)]
for i in range(N):
    x, y, d, g = map(int, input().split())

    q = deque([(y, x, d)])
    # init
    if d == 0:
        endpoint = [y, x+1]
    elif d == 1:
        endpoint = [y-1, x]
    elif d == 2:
        endpoint = [y, x-1]
    elif d == 3:
        endpoint = [y+1, x]
    # 세대만큼 반복
    for j in range(g):
        roll(endpoint, q)
    for j in q:
        y, x, d = j
        Map[y][x] = 1
    Map[endpoint[0]][endpoint[1]] = 1

count = 0
for i in range(100):
    for j in range(100):
        if Map[i][j] == 1 and Map[i][j+1] == 1 and Map[i+1][j] == 1 and Map[i+1][j+1] == 1:
            count += 1
print(count)
