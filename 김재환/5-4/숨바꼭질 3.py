"""
완전탐색을 이용하면 좋을것 같기는 하지만 N,K<=100,000 로 너무 크기 때문에 완탐 돌리기 부담스러움
1. DP 안됨
2. 다익스트라 : 
"""
import heapq
N, K = map(int, input().split())
INF = 1000000
dp = [INF for i in range(200002)]

dp[N] = 0
pq = [[0, N]]
while pq:
    print(pq)
    v, node = heapq.heappop(pq)
    if node > 100000:
        continue
    if node == K:
        print(v)
        break

    # adj node node-1, node+1, node//2
    if node*2 <= 100000 and v < dp[node*2]:
        dp[node*2] = v
        heapq.heappush(pq, [v, node*2])
    if node-1 >= 0 and v+1 < dp[node-1]:
        dp[node-1] = v + 1
        heapq.heappush(pq, [v+1, node-1])
    if node+1 < 100001 and v+1 < dp[node+1]:
        dp[node+1] = v + 1
        heapq.heappush(pq, [v+1, node+1])
