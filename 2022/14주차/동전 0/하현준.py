"""
동전 0
https://www.acmicpc.net/problem/11047
"""
import sys

sys.stdin = open("../input.txt")
for _ in range(int(input())):
    n, k = map(int, input().split())
    data = [int(input()) for _ in range(n)]
    total_count = 0

    for i in range(n - 1, -1, -1):
        if data[i] <= k:
            count = k // data[i]
            total_count += count
            k -= data[i] * count
    print(total_count)