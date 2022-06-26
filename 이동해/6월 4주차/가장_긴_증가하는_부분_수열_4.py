n = int(input())
data = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 길이 출력
m = max(dp)
print(m)

result = []
for i in range(n - 1, -1, -1):
    if dp[i] == m:
        result.append(data[i])
        m -= 1
        
result.reverse()
print(*result)
