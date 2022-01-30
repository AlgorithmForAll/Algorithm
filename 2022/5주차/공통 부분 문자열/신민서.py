one = input()
two = input()

dp = [[0 for _ in range(len(one)+1)] for _ in range(len(two)+1)]
answer = 0
for i in range(1, len(two)+1):
    for j in range(1, len(one)+1):
        if two[i-1] == one[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)