n = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)
res = []
for i in range(n):
    idx = temp.index(arr[i])
    # print(idx, temp)
    if idx in res:
        res.append(idx + 1)
    else:
        res.append(idx)
        temp[idx] = -1
print(*res)
