n = int(input())
arr = [0] * (n + 1)
path = [0] * (n + 1)

arr[1] = 0
path[1] = [1]

for i in range(2, n + 1):
    arr[i] = arr[i - 1] + 1
    path[i] = path[i - 1] + [i]

    if i % 3 == 0 and arr[i // 3] + 1 < arr[i]:
        arr[i] = arr[i // 3] + 1
        path[i] = path[i // 3] + [i]

    if i % 2 == 0 and arr[i // 2] + 1 < arr[i]:
        arr[i] = arr[i // 2] + 1
        path[i] = path[i // 2] + [i]
path[n].reverse()
print(arr[n])
print(*path[n])