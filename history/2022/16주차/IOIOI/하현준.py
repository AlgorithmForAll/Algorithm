"""
IOIOI
https://www.acmicpc.net/problem/5525
"""
import sys

sys.stdin = open("../input.txt")

# def get_pattern_table(p):
#     table = [0 for _ in range(len(p))]
#     j = 0
#     for i in range(1, len(p)):
#         while j > 0 and p[i] != p[j]:
#             j = table[j - 1]
#         if p[i] == p[j]:
#             j += 1
#             table[i] = j
#     return table


for _ in range(20):
    n = int(input())
    m = int(input())
    s = input()
    pattern = "IO" * n + "I"
    ptable = [0, 0] + [i for i in range(1, 2 * n)]

    count = 0
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = ptable[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                count += 1
                j = ptable[j]
            else:
                j +=1

    print(count)
