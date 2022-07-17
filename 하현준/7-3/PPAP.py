"""
https://www.acmicpc.net/problem/16120
"""
import sys

sys.stdin = open("../input.txt")
data = input()
result = []
ppap = ["P", "P", "A", "P"]
for d in data:
    result.append(d)
    if result[-4:] == ppap:
        for _ in range(3):
            result.pop()

if result == ppap or result == ["P"]:
    print("PPAP")
else:
    print("NP")
