"""
교점에 별 만들기
https://programmers.co.kr/learn/courses/30/lessons/87377
"""
from itertools import combinations


def get_location(line1, line2):
    A, B, E = line1
    C, D, F = line2
    if (A * D - B * C) == 0 or (A * D - B * C) == 0:
        return 0.1, 0.1
    return (B * F - E * D) / (A * D - B * C), (E * C - A * F) / (A * D - B * C)


def solution(line):
    locations = []
    for line1, line2 in combinations(line, 2):
        x, y = get_location(line1, line2)
        if x == int(x) and y == int(y):
            locations.append([int(x), int(y)])
    locations.sort(key=lambda x: (-x[1], x[0]))
    xs, ys = list(zip(*locations))
    minx, miny = min(xs), min(ys)
    maxx, maxy = max(xs), max(ys)

    answer = []
    for j in range(maxy, miny - 1, -1):
        temp = []
        for i in range(minx, maxx + 1):
            if [i,j] in locations:
                temp.append("*")
            else:
                temp.append(".")
        answer.append("".join(temp))
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]),
      ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........",
       "*.......*"])
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]), ["*.*"])
print(solution([[1, -1, 0], [2, -1, 0]]), ["*"])
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]), ["*"])
