"""
힙을 동기화하는 문제가 있었는데
이러한 문제는 visited로 해결하는 거였음. 어렵다
"""
import heapq
import sys
input = sys.stdin.readline


INF = 1000001

T = int(input())
for t in range(T):
    k = int(input())

    maxq = []
    minq = []
    visited = [0 for i in range(INF)]

    for k in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':  # insert
            heapq.heappush(maxq, (-num, k))
            heapq.heappush(minq, (num, k))
            visited[k] = 1
        else:  # delete
            if num == 1:
                while len(maxq) > 0 and visited[maxq[0][1]] == 0:
                    _num, _k = heapq.heappop(maxq)
                if len(maxq) != 0:
                    _num, _k = heapq.heappop(maxq)
                    visited[_k] = 0
            if num == -1:
                while len(minq) > 0 and visited[minq[0][1]] == 0:
                    _num, _k = heapq.heappop(minq)
                if len(minq) != 0:
                    _num, _k = heapq.heappop(minq)
                    visited[_k] = 0

    while len(maxq) > 0 and visited[maxq[0][1]] == 0:
        _num, _k = heapq.heappop(maxq)
    while len(minq) > 0 and visited[minq[0][1]] == 0:
        _num, _k = heapq.heappop(minq)

    if len(maxq) == 0:
        print("EMPTY")

    else:
        print(-heapq.heappop(maxq)[0], end=" ")
        print(heapq.heappop(minq)[0], )
