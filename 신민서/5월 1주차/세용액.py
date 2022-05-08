n = int(input())
arr = sorted(list(map(int, input().split())))
result = []
val = float('inf')
for i in range(len(arr)-2):
    s, e = i+1, len(arr)-1
    while s != e:
        new_val = arr[i] + arr[s] + arr[e]
        if abs(new_val) < abs(val):
            val = new_val
            result = [arr[i], arr[s], arr[e]]
        if new_val < 0:
            s += 1
        elif new_val > 0:
            e -= 1
        else:
            print(arr[i], arr[s], arr[e])
            exit()
result.sort()
print(*result)