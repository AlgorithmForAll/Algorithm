import heapq
import sys
input = sys.stdin.readline
N = int(input())

bigheap = []
smallheap = []

final = 10000

for _ in range(N):
    val = int(input())
    # final과 비교
    if val <= final:
        heapq.heappush(bigheap, -val)
    else:
        heapq.heappush(smallheap, val)
    # 개수 비교
    if len(bigheap) >= len(smallheap)+2:  # 오른족으로 옮기기
        tmp = -heapq.heappop(bigheap)
        heapq.heappush(smallheap, tmp)
    elif len(bigheap) < len(smallheap):
        tmp = heapq.heappop(smallheap)
        heapq.heappush(bigheap, -tmp)

    final = -bigheap[0]
    print(final)
