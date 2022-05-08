import heapq
import sys
input = sys.stdin.readline


N = int(input())
queue = []

for i in range(N):
    S, T = map(int, input().split())
    queue.append([S, T])

queue = sorted(queue, key = lambda x: (x[0] , x[1]))
q = []
heapq.heappush(q, queue[0][1])

for i in range(1, N):
    if queue[i][0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, queue[i][1])
    else:
        heapq.heappush(q, queue[i][1])

print(len(q))