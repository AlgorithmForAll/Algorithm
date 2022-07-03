"""
https://www.acmicpc.net/problem/13913
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
history = [0 for _ in range(100001)]


def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            data = []
            temp = now
            for _ in range(visited[now] + 1):
                data.append(temp)
                temp = history[temp]

            print(visited[now])
            print(*data[::-1], sep=" ")
            return

        for xx in (now - 1, now + 1, now * 2):
            if 0 <= xx <= 100000 and visited[xx] == 0:
                visited[xx] = visited[now] + 1
                history[xx] = now
                q.append(xx)


bfs()
