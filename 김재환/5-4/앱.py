"""
1. 경우의 수 구하기
2. 그래프로 경우의 수를 전부 포함하는 sub problem만들어보기
3. 점화식 만들기
4. dp로 가능하도록 만들어보기
5 60
30 10 20 35 40
3 0 3 5 4
"""

N, M = map(int, input().split())
Mem = [0] + list(map(int, input().split()))
Cost = [0] + list(map(int, input().split()))

dp = [[0 for i in range(sum(Cost)+1)] for i in range(N+1)]
answer = sum(Cost)
for i in range(1, N+1):
    for j in range(sum(Cost)+1):
        # cost 비교
        if 0 <= j - Cost[i]:
            dp[i][j] = max(dp[i-1][j-Cost[i]] + Mem[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M:
            answer = min(answer, j)
print(answer)
