n, k = map(int, input().split())
arr = [0 for _ in range(n)]
cnt = 0

for i in range(n):
    arr[i] = int(input())
for i in range(n-1, -1, -1):
    if k <= 0:
        break
    while k-arr[i] >= 0:
        k -= arr[i]
        cnt += 1

print(cnt)