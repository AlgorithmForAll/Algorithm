"""
위장
https://programmers.co.kr/learn/courses/30/lessons/42578
"""
from collections import defaultdict


def solution(clothes):
    answer = 1
    data = defaultdict(int)
    for cname, ctype in clothes:
        data[ctype] += 1

    for v in data.values():
        answer *= v + 1

    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]), 5)
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]), 3)
