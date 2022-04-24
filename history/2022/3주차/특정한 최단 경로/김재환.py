import heapq
import sys
input = sys.stdin.readline
N, E = map(int, input().split())

INF = 100000000
dp = [[INF for i in range(N+1)] for i in range(N+1)]
for i in range(E):
    # floid
    a, b, c = map(int, input().split())
    dp[a][b] = c
    dp[b][a] = c
    dp[a][a] = 0
    dp[b][b] = 0
a, b = map(int, input().split())


def daik(fnode):
    # 힙큐 사용
    hq = []
    heapq.heappush(hq, [0, fnode])  # 0거리값의 1노드에서 출발
    arr = [INF for i in range(N+1)]
    arr[fnode] = 0

    while hq:
        mcost, mnode = heapq.heappop(hq)
        for ei in range(N):
            enode = ei+1
            ecost = dp[mnode][enode]
            if arr[enode] > ecost + mcost:
                arr[enode] = ecost + mcost
                heapq.heappush(hq, [ecost + mcost, enode])
    return arr


# 1->A->B->N
result = min(daik(1)[a]+daik(a)[b]+daik(b)[N],
             daik(1)[b]+daik(b)[a]+daik(a)[N])
if result >= INF:
    print(-1)
else:
    print(result)

"""
# 플로이드 시간초과로 안됨
import sys
input = sys.stdin.readline
N, E = map(int, input().split())

INF = 100000000
dp = [[INF for i in range(N+1)] for i in range(N+1)]

for i in range(E):
    # floid
    a, b, c = map(int, input().split())
    dp[a][b] = c
    dp[b][a] = c
    dp[a][a] = 0
    dp[b][b] = 0
a, b = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if(i == j):
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


# 1 -> A -> B -> N  ////// # 1-> B -> A -> N
result = min(dp[1][a] + dp[a][b] + dp[b][N],
             dp[1][b] + dp[b][a] + dp[a][N])
if result >= INF:
    print(-1)
else:
    print(result)
"""
