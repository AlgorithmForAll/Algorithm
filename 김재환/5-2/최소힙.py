import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []
for n in range(N):
    cmd = int(input())
    if cmd == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, cmd)
