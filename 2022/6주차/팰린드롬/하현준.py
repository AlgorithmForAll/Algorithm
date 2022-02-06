"""
팰린드롬?
https://www.acmicpc.net/problem/10942
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline  # 시간 초과 해결!


def check(left, right):
    while left <= right:
        if (left, right) in dp:
            return True
        if nums[left] == nums[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
dp = set()
result = []
for _ in range(m):
    s, e = map(int, input().split())
    if check(s - 1, e - 1):
        dp.add((s - 1, e - 1))
        result.append(1)
    else:
        result.append(0)

print(*result, sep="\n")
