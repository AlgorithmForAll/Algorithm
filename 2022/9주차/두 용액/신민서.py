n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = len(arr)-1
inf = float('inf')
ans = inf
answer = []
while left < right:
    if abs(arr[left] + arr[right]) < abs(ans):
        answer = [arr[left], arr[right]]
        ans = arr[left] + arr[right]
    if arr[left] + arr[right] < 0:
        left += 1
    elif arr[left] + arr[right] > 0:
        right -= 1
    else:
        break
print(answer[0], answer[1])