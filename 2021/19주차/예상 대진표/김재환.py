import math


def solution(n, a, b):
    answer = 0

    for i in range(int(n/2)):
        A = math.ceil(a/2)
        B = math.ceil(b/2)
        if A == B:  # 만남
            return i+1
        a = A
        b = B
    return 0
