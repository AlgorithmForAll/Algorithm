import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []

for i in range(N):
    tmp = int(input())

    if tmp == 0:  # 출력
        if len(q) > 0:
            absV, V = heapq.heappop(q)
            print(V)
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(tmp), tmp))
