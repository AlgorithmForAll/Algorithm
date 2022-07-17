"""
https://www.acmicpc.net/problem/21608
"""
import heapq
import sys
from collections import defaultdict

sys.stdin = open("../input.txt")


def get_seats(now):
    seat = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                empty = 0
                likes = 0
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        who = graph[xx][yy]
                        if who == 0:
                            empty += 1
                        elif who in data[now]:
                            likes += 1
                heapq.heappush(seat, (-likes, -empty, i, j))
    return heapq.heappop(seat)


def get_satifactions():
    total = 0
    for i in range(n):
        for j in range(n):
            who = graph[i][j]
            count = 0
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                if 0 <= xx < n and 0 <= yy < n:
                    if graph[xx][yy] in data[who]:
                        count += 1
            total += satisfaction[count]
    return total


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
data = defaultdict(list)
satisfaction = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n ** 2):
    temp = list(map(int, input().split()))
    data[temp[0]] = temp[1:]
    seat_data = get_seats(temp[0])
    graph[seat_data[2]][seat_data[3]] = temp[0]

print(get_satifactions())
