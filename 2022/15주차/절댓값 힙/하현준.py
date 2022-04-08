"""
절댓값 힙
https://www.acmicpc.net/problem/11286
"""
import heapq
import sys

sys.stdin = open("../input.txt")

input = sys.stdin.readline

neg_heap = []
pos_heap = []
answer = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if neg_heap and not pos_heap:
            answer.append(-heapq.heappop(neg_heap))
        elif not neg_heap and pos_heap:
            answer.append(heapq.heappop(pos_heap))
        elif neg_heap and pos_heap:
            nx = heapq.heappop(neg_heap)
            px = heapq.heappop(pos_heap)
            if abs(nx) > abs(px):
                answer.append(px)
                heapq.heappush(neg_heap, nx)
            elif abs(nx) <= abs(px):
                answer.append(-nx)
                heapq.heappush(pos_heap, px)
        else:
            answer.append(0)
    elif x < 0:
        heapq.heappush(neg_heap, -x)
    elif x > 0:
        heapq.heappush(pos_heap, x)

print(*answer, sep="\n")
