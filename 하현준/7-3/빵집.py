"""
https://www.acmicpc.net/problem/3109
"""
import sys

sys.stdin = open("../input.txt")


def get_path(i, j):
    if j == c - 1 and graph[i][j] == ".":
        return True

    for k in range(3):
        xx = i + dx[k]
        yy = j + dy[k]
        if 0 <= xx < r and 0 <= yy < c:
            if graph[xx][yy] == "." and visited[xx][yy] == 0:
                visited[xx][yy] = 1
                if get_path(xx, yy):
                    return True

    return False


dx = [-1, 0, 1] # greedy : 탐색 순서
dy = [1, 1, 1]
r, c = map(int, input().split())
answer = 0
graph = []
for i in range(r):
    graph.append(list(input()))

visited = [[0 for _ in range(c)] for _ in range(r)]

for s in range(r):
    if get_path(s, 0):
        answer += 1

print(answer)
