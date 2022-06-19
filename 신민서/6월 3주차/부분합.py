N, S = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 0
s = arr[0]
length = 987654321
while True:
    if s >= S:
        length = min(length, r - l + 1)
        s -= arr[l]
        l += 1
    else:
        if r >= N-1:
            break
        r += 1
        s += arr[r]
if length == 987654321:
    print(0)
else:
    print(length)