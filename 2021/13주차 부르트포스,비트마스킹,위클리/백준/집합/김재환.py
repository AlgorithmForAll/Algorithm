"""
비트마스킹은 그냥 값을 배열 flag처럼 처리하는 건가?
"""

import sys
input = sys.stdin.readline
M = int(input())
S = [0 for i in range(0, 21)]
for i in range(M):
    tmp = input()
    if tmp == "all\n":
        cmd = "all"
    elif tmp == "empty\n":
        cmd = "empty"
    else:
        cmd, num = tmp.split()
        num = int(num)

    if cmd == "add":
        S[num] = 1
    elif cmd == "remove":
        S[num] = 0
    elif cmd == "check":
        if S[num] == 1:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        S[num] = S[num] ^ 1
    elif cmd == "all":
        S = [1 for i in range(0, 21)]
    else:  # empty
        S = [0 for i in range(0, 21)]
