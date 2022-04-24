import heapq
n = int(input())
q = []
for i in range(n):
    inp = int(input())
    if inp == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(inp), inp))