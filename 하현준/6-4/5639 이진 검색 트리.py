"""
https://www.acmicpc.net/problem/5639
"""
from operator import le
import sys

sys.stdin = open("../input.txt")
sys.setrecursionlimit(10 ** 6)


def post_order(start, end):
    if start >= end:
        return

    root = pre_order[start]
    if pre_order[end - 1] <= root:
        post_order(start + 1, end)
        print(root)
        return

    left_child_idx = 0
    for i in range(start + 1, end):
        if pre_order[i] > root:
            left_child_idx = i
            break

    post_order(start + 1, left_child_idx)
    post_order(left_child_idx, end)
    print(root)


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        post_order(0, len(pre_order))
        break
