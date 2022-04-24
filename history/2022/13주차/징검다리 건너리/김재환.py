"""
dp 갱신을 안해서 헤맸다....
"""
N = int(input())
J = []
if N != 1:
    for i in range(N-1):
        a, b = map(int, input().split())
        J.append([a, b])
K = int(input())

if N == 1:
    print(0)
    exit()


# 매우 큰 점프 안하는 경우
INF = 10**10
answer = INF

dp = [INF for i in range(N)]
dp[0] = 0
for i in range(1, N):
    si = i-1
    bi = i-2
    sv, bv = INF, INF
    if 0 <= si:
        sv = dp[si] + J[si][0]
    if 0 <= bi:
        bv = dp[bi] + J[bi][1]
    dp[i] = min(sv, bv)

answer = min(answer, dp[-1])

_dp = []
for i in dp:
    _dp.append(i)

# K값을 뛰는 경우
for t in range(N-3):
    start = t+3
    _dp[start] = _dp[t] + K
    for i in range(t+4, N):
        si = i-1
        bi = i-2
        sv, bv = INF, INF
        if start <= si:
            sv = _dp[si] + J[si][0]
        if start <= bi:
            bv = _dp[bi] + J[bi][1]
        _dp[i] = min(sv, bv)
    answer = min(answer, _dp[-1])
    _dp = []
    for i in dp:
        _dp.append(i)

print(answer)
