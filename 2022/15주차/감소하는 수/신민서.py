t = int(input())

for tt in range(t):
    n = int(input())
    arr = [[0 for _ in range(2)] for __ in range(n)]
    for i in range(n):
        a, b = map(int, input().split())
        arr[i][0] = a
        arr[i][1] = b
    arr.sort()
    cnt = 1
    now = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < now:
            cnt += 1
            now = arr[i][1]
    print(cnt)