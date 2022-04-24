"""
1년 2월 탄생
매년 1월 분열
홀: 3번 분열 사망
짝: 4번 분열 사망
dp
"""
dp = [[0, 0], [1, 0], [1, 1], [3, 1]]

N = int(input())
for i in range(4, N+1):

    dp.append(list(dp[i-1]))
    if i % 2 == 0:
        dp[i][1] += sum(dp[i-1])
    else:
        dp[i][0] += sum(dp[i-1])

    h = dp[i-3][0]  # 홀수
    for j in range(i-3, i+1):
        dp[j][0] -= h

    z = dp[i-4][1]
    for j in range(i-4, i+1):
        dp[j][1] -= z
print(sum(dp[N]))
