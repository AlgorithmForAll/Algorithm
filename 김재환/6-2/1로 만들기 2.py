"""
DP로 하면 순서대로 출력이 안된다.
dp로 다시 확인하게 하는수밖에...
dp로 만들어도 되는게 다시 뒤에서부터 작은 수를 찾아 확인하면 된다.
"""
N = int(input())

dp = [i for i in range(N+1)]
dp[1] = 0
# dp 구하기
for n in range(2, N+1):
    if n % 3 == 0:
        dp[n] = min(dp[n], dp[n//3]+1)
    if n % 2 == 0:
        dp[n] = min(dp[n], dp[n//2]+1)
    dp[n] = min(dp[n], dp[n-1]+1)

print(dp[N])
tmp = []
# 순서구하기
while True:
    n = N
    tmp.append(n)
    if n <= 1:
        break
    if N % 3 == 0:
        if dp[n] > dp[N//3]:
            n = N//3
    if N % 2 == 0:
        if dp[n] > dp[N//2]:
            n = N//2
    if dp[n] > dp[N-1]:
        n = N-1
    N = n
print(" ".join(map(str, tmp)))
