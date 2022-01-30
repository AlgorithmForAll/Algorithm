a = input()
b = input()
if len(a) > len(b):
    c = a
    a = b
    b = c
dp = [[0 for i in range(len(a)+1)] for i in range(len(b)+1)]
maxdp = 0
for i in range(0, len(b)):
    for j in range(0, len(a)):
        di = i+1
        dj = j+1
        if b[i] == a[j]:  # 같은게 있으면 추가
            dp[di][dj] = dp[di-1][dj-1] + 1
        else:
            dp[di][dj] = 0
        maxdp = max(maxdp, dp[di][dj])
print(maxdp)
