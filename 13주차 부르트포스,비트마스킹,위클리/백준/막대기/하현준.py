"""
막대기
https://www.acmicpc.net/problem/1094

import heapq

x = int(input())
bar = []

heapq.heappush(bar, 64)

while sum(bar) > x:
    min_bar = heapq.heappop(bar)
    heapq.heappush(bar, min_bar // 2)
    if sum(bar) < x:
        heapq.heappush(bar, min_bar // 2)

print(len(bar))
"""
# 비트마스킹 방식으로 풀어보자
print(bin(int(input())).count("1"))
