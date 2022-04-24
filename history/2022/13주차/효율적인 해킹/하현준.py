"""
효율적인 해킹
https://www.acmicpc.net/problem/1325
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 5)


def bfs(start):
    q = deque([start])
    result = 0
    while q:
        now = q.popleft()
        for node in path[now]:
            if visited[node] == 0:
                visited[node] = 1
                result += 1
                q.append(node)

    return result

# 시간 초과
def dfs(i, history):
    if not path[i]:
        return history

    ret = {i}
    for node in path[i]:
        if visited[node] == 0:
            visited[node] = 1
            ret |= dfs(node, history | {node})
            visited[node] = 0
    return ret


inf = float('inf')
for _ in range(int(input())):
    n, m = map(int, input().split())
    path = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        path[b].append(a)

    result = []
    max_count = -1

    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        visited[i] = 1
        count = bfs(i)

        # count = dfs(i, {i})
        # count = len(count)

        if max_count < count:
            max_count = count
            result = [str(i)]
        elif max_count == count:
            result.append(str(i))

    print(" ".join(result))
