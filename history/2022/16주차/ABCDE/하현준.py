"""
ABCDE
https://www.acmicpc.net/problem/13023
"""
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(now):
    if len(data) == 5:
        print(1)
        exit()
        return

    for node in friend[now]:
        if visited[node] == 0:
            visited[node] = 1
            data.append(node)
            dfs(node)
            data.pop()
            visited[node] = 0


for _ in range(4):
    n, m = map(int, input().split())
    friend = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a].append(b)
        friend[b].append(a)

    visited = [0 for _ in range(n)]
    data = []
    for i in range(n):
        visited[i] = 1
        data.append(i)
        dfs(i)
        data.pop()
        visited[i] = 0
    print(0)
