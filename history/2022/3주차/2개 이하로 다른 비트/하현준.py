"""
2개 이하로 다른 비트
https://programmers.co.kr/learn/courses/30/lessons/77885
"""


def f(x):
    min_bit = x & (-x)
    if min_bit > 1:
        answer = x + 1

    elif len(bin(x + 1)) - len(bin(x)) == 1:  # 111..1
        a = x + 1  # 1000
        b = (a >> 1) - 1  # 100 - 001 = 011
        answer = a + b
    else:
        x_bit = bin(x)[2:]
        for i in range(len(x_bit) - 1, -1, -1):
            if x_bit[i] == "0":
                x ^= (1 << (len(x_bit) - i - 1))
                if i + 1 < len(x_bit) and x_bit[i + 1] == "1":
                    x ^= (1 << (len(x_bit) - i - 2))
                break
        answer = x
    return answer


def solution(numbers):
    return [f(x) for x in numbers]


print(solution([2, 7, 185, 0, 999, 65535]), [3, 11])
