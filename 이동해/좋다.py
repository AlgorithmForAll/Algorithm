n = int(input())
numbers = list(map(int, input().split()))

# 오름차순 정렬
numbers.sort()

count = 0

for i in range(n):
    arr = numbers[:i] + numbers[i + 1:]
    # 투포인터 사용
    left, right = 0, n - 2
    while left < right:
        temp = arr[left] + arr[right]
        if temp == numbers[i]:
            count += 1
            break
        if temp < numbers[i]:
            left += 1
        else:
            right -= 1
print(count)
