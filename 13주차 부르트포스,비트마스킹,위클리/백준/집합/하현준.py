"""
집합
https://www.acmicpc.net/problem/11723
"""
import sys

input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    d = input().split()
    oper = d[0]
    if oper == "all":
        result = (1 << 20) - 1
    elif oper == "empty":
        result = 0
    else:
        num = int(d[1]) - 1
        if oper == "add":
            if not result & (1 << num):
                result |= (1 << num)
        elif oper == "remove":
            if result & (1 << num):
                result &= ~(1 << num)
        elif oper == "check":
            if result & (1 << num):
                print(1)
            else:
                print(0)
        elif oper == "toggle":
            if result & (1 << num):
                result &= ~(1 << num)
            else:
                result |= (1 << num)
