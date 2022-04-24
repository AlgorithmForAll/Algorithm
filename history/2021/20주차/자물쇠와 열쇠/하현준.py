"""
자물쇠와 열쇠
https://programmers.co.kr/learn/courses/30/lessons/60059
"""


def solution(key, lock):
    n = len(lock)
    m = len(key)

    for i in range(-m + 1, n):
        for j in range(-m + 1, n):
            for _ in range(4):
                for x in range(m):
                    for y in range(m):
                        xx = x + i
                        yy = y + j
                        if 0 <= xx < n and 0 <= yy < n:
                            lock[xx][yy] += key[x][y]

                temp = sum(lock, [])
                if 0 not in temp and 2 not in temp:
                    return True

                for x in range(m):
                    for y in range(m):
                        xx = x + i
                        yy = y + j
                        if 0 <= xx < n and 0 <= yy < n:
                            lock[xx][yy] -= key[x][y]
                key = list(map(list, zip(*key[::-1])))
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
