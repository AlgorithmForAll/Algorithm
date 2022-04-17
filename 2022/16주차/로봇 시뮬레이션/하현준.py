"""
로봇 시뮬레이션
https://www.acmicpc.net/problem/2174
"""
import sys

sys.stdin = open("../input.txt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = {'N': 1, 'E': 2, 'S': 3, 'W': 0}

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[0 for _ in range(b)] for _ in range(a)]
data = []
robots = [[]]
for i in range(n):
    x, y, r = input().split()
    x = int(x) - 1
    y = int(y) - 1
    robots.append([x, y, direction[r]])
    graph[x][y] = i + 1

for _ in range(m):
    robot, oper, loop = input().split()
    robot = int(robot)
    loop = int(loop)
    rx, ry, rd = robots[robot]

    if oper == "F":
        graph[rx][ry] = 0
        xx = rx
        yy = ry
        for _ in range(loop):
            xx += dx[rd]
            yy += dy[rd]
            if 0 <= xx < a and 0 <= yy < b:
                if graph[xx][yy] != 0:
                    robots[robot] = [xx - dx[rd], yy - dy[rd], rd]
                    graph[xx - dx[rd]][yy - dy[rd]] = robot
                    data.append(f"Robot {robot} crashes into robot {graph[xx][yy]}")
                    print(f"robot crash {robot=}->{graph[xx][yy]}")
                    break

            else:
                robots[robot] = [xx - dx[rd], yy - dy[rd], rd]
                graph[xx - dx[rd]][yy - dy[rd]] = robot
                data.append(f"Robot {robot} crashes into the wall")
                print(f"wall crash {robot=}")
                break
        else:
            robots[robot] = [xx,yy, rd]
            graph[xx][yy] = robot
    elif oper == "L":
        for _ in range(loop):
            rd -= 1
            if rd < 0:
                rd = 3
        robots[robot] = [rx, ry, rd]
    elif oper == "R":
        for _ in range(loop):
            rd += 1
            if rd >= 4:
                rd = 0
        robots[robot] = [rx, ry, rd]

print(data[0] if data else "OK")
