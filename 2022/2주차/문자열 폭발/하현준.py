"""
문자열 폭발
https://www.acmicpc.net/problem/9935
"""

from collections import deque

word = deque(input())
bomb = list(input())[::-1]
n = len(bomb)
stack = []
while word:
    w = word.pop()
    stack.append(w)
    # print(stack,end=" -> ")
    if len(stack) >= n:
        if stack[-1] == bomb[-1] and stack[-n:] == bomb:
            for _ in range(n):
                stack.pop()
    # print(stack)

print("".join(stack[::-1]) if stack else "FRULA")