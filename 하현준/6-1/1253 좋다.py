"""
https://www.acmicpc.net/problem/1253
"""
import sys

sys.stdin = open("../input.txt")

n = int(input())
if n <= 2:
    print(0)
    exit()

arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(n):
    temp = arr[:i] + arr[i + 1:]
    left = 0
    right = n - 2

    while left < right:
        data = temp[left] + temp[right]
        if data == arr[i]:
            answer += 1
            break

        if data > arr[i]:
            right -= 1
        else:
            left += 1
print(answer)
