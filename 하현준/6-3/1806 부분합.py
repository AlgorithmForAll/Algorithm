"""
https://www.acmicpc.net/problem/1806
"""
import sys

sys.stdin = open("../input.txt")
inf = float('inf')
answer = inf
n, s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n - 1):
    arr[i + 1] += arr[i]
arr = [0] + arr

left = 0
right = 1
while left < right < n + 1:
    if arr[right] - arr[left] < s:
        right += 1
    elif arr[right] - arr[left] >= s:
        answer = min(answer, abs(right - left))
        left += 1

print(answer if answer != inf else 0)
