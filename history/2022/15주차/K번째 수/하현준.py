"""
K번째 수
https://www.acmicpc.net/problem/1300
참고 : https://hongcoding.tistory.com/13
"""
import sys

sys.stdin = open("../input.txt")
for _ in range(6):
    n = int(input())
    k = int(input())
    lo = 1
    hi = k
    while lo < hi:
        mid = (lo + hi) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, n)

        if count >= k:
            hi = mid
        else:
            lo = mid + 1

    print(lo)
