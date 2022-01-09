"""
각 격우의 수 = 경우의수 + 1(안입는 경우)
모든 경우의 수 *= 각 경우의 수 
"""


def solution(clothes):
    answer = 1
    Map = {}

    for tmp in clothes:
        cloth, kind = tmp
        if kind not in Map:
            Map[kind] = []
        Map[kind].append(cloth)
    print(Map)
    for key in Map.keys():
        print(key)
        tmp = Map[key]
        print(tmp)
        answer *= (len(tmp)+1)
    return answer - 1
