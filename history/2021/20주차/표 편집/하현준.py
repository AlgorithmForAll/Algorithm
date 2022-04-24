"""
표 편집
https://programmers.co.kr/learn/courses/30/lessons/81303
"""
from collections import deque


def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    linked = [[None, 0, 1]] + [[i - 1, i, i + 1] for i in range(1, n - 1)] + [[n - 2, n - 1, None]]
    record = deque([])
    now = k

    for i in range(len(cmd)):
        c1 = cmd[i][0]
        if c1 == "D":
            x = int(cmd[i][2:])
            while x > 0:
                x -= 1
                left, mid, right = linked[now]
                if right is None:
                    break
                now = right

        elif c1 == "U":
            x = int(cmd[i][2:])
            while x > 0:
                x -= 1
                left, mid, right = linked[now]
                if left is None:
                    break
                now = left

        elif c1 == "C":
            record.appendleft(now)
            left, mid, right = linked[now]
            if left is not None:
                linked[left][2] = right
            if right is not None:
                linked[right][0] = left
                now = right
            else:
                now = left

        elif c1 == "Z":
            rnum = record.popleft()
            left, mid, right = linked[rnum]
            if left is not None:
                linked[left][2] = rnum
            if right is not None:
                linked[right][0] = rnum

        print(linked, record, cmd[i], f"{now=}")

    while record:
        rnum = record.popleft()
        answer[rnum] = "X"
    return "".join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]), "OOOOXOOO")
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]), "OOXOXOOO")
