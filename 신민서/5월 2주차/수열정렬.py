n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
index = 0
for i in range(n):
    ans[arr.index(min(arr))] = index
    index += 1
    arr[arr.index(min(arr))] = 1001

for a in ans:
    print(a)