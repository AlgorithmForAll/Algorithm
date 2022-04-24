n, k = map(int, input().split())
li = []
for i in range(n):
    li.append(int(input()))

li.sort()
arr = [10001 for _ in range(k+1)]
arr[0] = 0

for num in li:
    for j in range(num, k+1):
        arr[j] = min(arr[j-num] + 1, arr[j])
if arr[k] != 10001:
    print(arr[k])
else:
    print(-1)