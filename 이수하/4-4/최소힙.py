import heapq
import sys
input = sys.stdin.readline


N = int(input())

heap = []
for i in range(N):
    X = int(input())
    if abs(X) != 0:
        heapq.heappush(heap, X)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))