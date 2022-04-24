"""
https://www.acmicpc.net/problem/16171
"""
import sys

sys.stdin = open("../input.txt")

s = input()
k = input()
s = "".join([x for x in s if not x.isnumeric()])
print(1 if k in s else 0)
