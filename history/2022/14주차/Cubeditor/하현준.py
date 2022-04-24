"""
Cubeditor
https://www.acmicpc.net/problem/1701
"""
import sys

sys.stdin = open("../input.txt")


def get_pattern_table(p):
    table = [0 for _ in range(len(p))]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

    return table


for _ in range(int(input())):
    count = 0
    data = input()
    for i in range(len(data)):
        table = get_pattern_table(data[i:])
        count = max(count, max(table))
    print(count)
