"""
스타트 택시
https://www.acmicpc.net/problem/19238
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_passenger(startx, starty):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    data = []
    visited[startx][starty] = 1
    q = deque([[startx, starty, fuel, 0]])

    while q:
        x, y, f, dist = q.popleft()
        if (x, y) in passenger:
            data.append([dist, x, y, f])
            if len(data) == len(passenger):
                break
            continue

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if graph[xx][yy] == 0 and visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    q.append([xx, yy, f - 1, dist + 1])
    if not data:
        return None
    data.sort()
    return data[0]


def drive(startx, starty, endx, endy):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[startx][starty] = 1
    q = deque([[startx, starty, 0]])

    while q:
        x, y, dist = q.popleft()
        if [x, y] == [endx, endy]:
            return dist
        if dist > fuel:  # 문제를 잘 읽자!
            return -1
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if graph[xx][yy] == 0 and visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    q.append([xx, yy, dist + 1])

    return -1


for _ in range(int(input())):
    n, m, fuel = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    tx, ty = map(int, input().split())
    tx -= 1
    ty -= 1
    passenger = []
    destination = dict()
    for _ in range(m):
        px, py, ex, ey = map(int, input().split())
        passenger.append((px - 1, py - 1))
        destination[(px - 1, py - 1)] = [ex - 1, ey - 1]

    while passenger:
        temp = find_passenger(tx, ty)
        if temp is None:
            fuel = -1
            break
        _, tx, ty, fuel = temp
        passenger.remove((tx, ty))
        ex, ey = destination[(tx, ty)]
        dist = drive(tx, ty, ex, ey)
        tx = ex
        ty = ey
        if dist == -1:
            fuel = -1
            break
        else:
            fuel += dist

    print(fuel)
