"""
DP
"""
N = int(input())
tmp = [0] + list(map(int, input().split()))

dp = [0 for i in range(N+1)]
dp[0] = 0
maxCount = 0
maxIndex = 0
for i in range(N+1):

    for j in range(i):
        if tmp[j] < tmp[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > maxCount:
                maxCount = dp[i]
                maxIndex = i


print(dp[maxIndex])
answer = [tmp[maxIndex]]
C = maxCount
for i in range(maxIndex-1, -1, -1):
    if dp[i] == C-1:
        answer.append(tmp[i])
        C = dp[i]

answer.reverse()
print(" ".join(map(str, answer[1:])))
