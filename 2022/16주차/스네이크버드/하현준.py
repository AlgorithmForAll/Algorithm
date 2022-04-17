"""
스네이크버드
https://www.acmicpc.net/problem/16435
"""
import sys

sys.stdin = open("../../input.txt")
n, l = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
for height in heights:
    if height <= l:
        l += 1

print(l)
