"""
크게 만들기
https://www.acmicpc.net/problem/2812
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")

for _ in range(10):
    n, k = map(int, input().split())
    num = deque(input())
    result = deque([num.popleft()])
    while num:
        now = num.popleft()
        if result[-1] < now:
            while k > 0 and result and result[-1] < now:
                result.pop()
                k -= 1
            result.append(now)
        elif result[-1] >= now:
            result.append(now)

    print("".join(result)[:len(result) - k])
