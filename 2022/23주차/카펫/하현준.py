"""
카펫
https://programmers.co.kr/learn/courses/30/lessons/42842
"""


def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yvert = i
            yhori = yellow // yvert

            hori = yhori + 2
            vert = yvert + ((brown - yvert * 2) // (yhori + 2))
            if (brown - yvert * 2) % hori == 0 and hori >= vert:
                return [hori, vert]


print(solution(10, 2), [4, 3])
print(solution(8, 1), [3, 3])
print(solution(24, 24), [8, 6])
