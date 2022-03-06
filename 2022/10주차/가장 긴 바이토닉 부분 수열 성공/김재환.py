"""
10
1 5 2 1 4 3 4 5 2 1
+ dp
- dp 
두개 구해서 총합이 가장 큰놈 구하기 - 1(자신을 중복포함하기 때문) 
"""

N = int(input())
tmp = list(map(int, input().split()))
dp1 = [1 for i in range(N)]
dp2 = [1 for i in range(N)]


def calc(dp):
    for i in range(N):
        for j in range(0, i):
            if tmp[i] > tmp[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp


dp1 = calc(dp1)
tmp = tmp[::-1]
dp2 = calc(dp2)[::-1]
final = 0
for i in range(N):
    final = max(final, dp1[i]+dp2[i])
print(final-1)
