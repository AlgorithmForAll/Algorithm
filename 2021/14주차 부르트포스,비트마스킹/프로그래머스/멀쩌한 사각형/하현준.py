"""
멀쩡한 사각형
https://programmers.co.kr/learn/courses/30/lessons/62048
"""
import math


# 15,16 시간 초과
def solution(w, h):
    if w == 1 or h == 1:
        return 0
    gcd = math.gcd(w, h)
    gw, gh = w // gcd, h // gcd
    count = 0

    coords = [(0.0, 0.0)]
    for i in range(1, gh):
        coords.append(((gw / gh) * i, float(i)))
    for j in range(1, gw):
        coords.append((float(j), (gh / gw) * j))
    coords.append((float(gw), float(gh)))
    coords.sort()

    for i in range(len(coords) - 1):
        a, b = coords[i], coords[i + 1]
        ax, ay = math.floor(a[0]), math.floor(a[1])
        bx, by = math.ceil(b[0]), math.ceil(b[1])
        if [ax + 1, ay + 1] == [bx, by]:
            count += 1
    return w * h - gcd * count


# ㅋㅋㅋ
def solution(w, h):
    t = math.gcd(w, h)
    return w * h - (w + h - t)


print(solution(8, 12))
print(solution(12, 8))
print(solution(5, 8))
print(solution(8, 5))
print(solution(2, 2))
