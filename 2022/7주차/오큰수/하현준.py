"""
오큰수
https://www.acmicpc.net/problem/17298
"""
from collections import deque
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result = deque([-1])
    stack = [arr.pop()]
    while arr:
        now = arr.pop()
        while stack:
            val = stack.pop()
            if val > now:
                stack.append(val)
                stack.append(now)
                result.appendleft(val)
                break
        else:
            stack.append(now)
            result.appendleft(-1)

    for r in result:
        print(r,end=" ")
    print()