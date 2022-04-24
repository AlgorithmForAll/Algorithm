"""
Contact
https://www.acmicpc.net/problem/1013
"""

import sys, re

sys.stdin = open("../input.txt")
input = sys.stdin.readline
# p = re.compile("(100|11)+")  # (100 | 11)+
# p = re.compile("(10+1)+")  # (10+1)+

result = []
p = re.compile("(100+1+|01)+")  # (100+1+|01)+
for _ in range(int(input())):
    data = input().rstrip()
    m = p.fullmatch(data)
    result.append("YES" if m else "NO")
print(*result, sep="\n")
