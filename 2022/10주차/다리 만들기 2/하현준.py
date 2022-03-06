"""
다리 만들기 2
https://www.acmicpc.net/problem/17472
"""
from collections import deque
from itertools import combinations
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def get_island():
    islands = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] == 1:
                visited[i][j] = 1
                island = [[i, j]]
                q = deque([[i, j]])

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < m:
                            if visited[xx][yy] == 0 and graph[xx][yy] == 1:
                                visited[xx][yy] = 1
                                island.append([xx, yy])
                                q.append([xx, yy])

                islands.append(island)
    return dict(enumerate(islands))


def get_paths(a_island, b_island):
    paths = []

    for ax, ay in a_island:
        for k in range(4):
            path = []
            q = deque([[ax, ay]])

            while q:
                x, y = q.popleft()

                while True:
                    x += dx[k]
                    y += dy[k]
                    if not (0 <= x < n and 0 <= y < m):
                        break
                    if [x, y] in a_island:
                        break
                    if [x, y] in b_island:
                        if len(path) >= 2:
                            paths.append(path)
                        break

                    if graph[x][y] == 0:
                        path.append([x, y])
                    else:
                        break

    return paths


def spaning_tree(edges):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    parent = [i for i in range(len(islands))]
    edges.sort()
    result = 0
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    for i in range(len(islands)):
        parent[i] = find_parent(parent, parent[i])

    return result if len(set(parent)) == 1 else -1


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    islands = get_island()
    path_dict = dict()
    edges = []
    for case in combinations(islands.keys(), 2):
        a, b = case
        paths = get_paths(islands[a], islands[b])
        if paths:
            path_dict[(a, b)] = paths
            edges.append([len(min(paths, key=len)), a, b])

    print(spaning_tree(edges))
