"""
강의실 배정
https://www.acmicpc.net/problem/11000
"""
import sys, heapq

sys.stdin = open("../input.txt")
input = sys.stdin.readline
for _ in range(10):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: (x[0]))
    q = []
    count = 0

    for s, e in data:
        if not q:
            count += 1
            heapq.heappush(q, (e, count))
        else:
            be, bcount = heapq.heappop(q)
            if be <= s:
                heapq.heappush(q, (e, bcount))
            else:
                heapq.heappush(q, (be, bcount))
                count += 1
                heapq.heappush(q, (e, count))
    print(count)