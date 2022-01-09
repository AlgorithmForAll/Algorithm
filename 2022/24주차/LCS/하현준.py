"""
LCS
https://www.acmicpc.net/problem/9251
참고 : https://www.youtube.com/watch?v=EAXDUxVYquY
"""
word_a = input()
word_b = input()
dp = [[0 for _ in range(len(word_a) + 1)] for _ in range(len(word_b) + 1)]

for i in range(len(word_b)):
    for j in range(len(word_a)):
        if word_b[i] == word_a[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
print(dp[len(word_b)][len(word_a)])