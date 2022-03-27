"""
1. 소수 구하기(N까지) => 에라토스테네스의 체로 한번에 싹다 구하기
2. 투포인터로 올바른것 구하기
3. 제한은 R < target
"""

N = int(input())

dp = [-1 for i in range(N+1)]
prime = []
for i in range(2, N+1):

    if dp[i] == -1:
        dp[i] = 1
        prime.append(i)
        for j in range(2, N//i+1):
            dp[i*j] = 0

# 투포인터
L = 0
R = 0
count = 0
while L <= R < len(prime):
    val = sum(prime[L:R+1])
    if val == N:
        count += 1
        R += 1
    elif val < N:
        R += 1
    elif val > N:
        L += 1
print(count)
