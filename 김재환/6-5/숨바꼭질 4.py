
"""
BFS형태로 일단 몇번째인지 찾으며 dp 만들기
이후 K기준으로 거꾸로 DFS 진행하여 N도달시까지 데이터 뽑아내기
BFS + DP
"""

from collections import deque
N, K = map(int, input().split())

INF = 1000000
dp = [INF for i in range(100002*10)]


def BFS():
    q = deque([N])
    dp[N] = 0
    count = 0
    while q:
        count += 1
        for _ in range(len(q)):
            t = q.popleft()
            if t == K:
                return count

            if t-1 >= 0:
                if dp[t-1] == INF:
                    q.append(t-1)
                dp[t-1] = min(dp[t-1], count)

            if t+1 <= 100000:
                if dp[t+1] == INF:
                    q.append(t+1)
                dp[t+1] = min(dp[t+1], count)

            if t*2 <= 100000:
                if dp[t*2] == INF:
                    q.append(t*2)
                dp[t*2] = min(dp[t*2], count)


BFS()
print(dp[K])
answer = [K]
start = K
while start != N:
    dp[start]
    if dp[start - 1] == dp[start]-1:
        start = start-1
        answer.append(start)
        continue
    if dp[start + 1] == dp[start]-1:
        start = start+1
        answer.append(start)

        continue
    if start % 2 == 0 and dp[start//2] == dp[start]-1:
        start = start//2
        answer.append(start)

        continue

answer.reverse()
print(" ".join(map(str, answer)))
