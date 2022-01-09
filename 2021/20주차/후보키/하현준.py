"""
후보키
https://programmers.co.kr/learn/courses/30/lessons/42890
"""
from itertools import combinations
from collections import defaultdict


def check(case, data):
    case = list(case)
    data = sum(data.values(), [])
    for i in range(1, len(case) + 1):
        for ccase in combinations(case, i):
            if list(ccase) in data:
                return False
    return True


def solution2(relation):
    data = defaultdict(list)
    r = len(relation)
    c = len(relation[0])
    cols = list(map(list, zip(*relation)))
    arr = [i for i in range(c)]

    for i in range(1, c + 1):
        for case in combinations(arr, i):
            if check(case, data):
                temp = list(map(list, zip(*[cols[x] for x in case])))
                temp = ["_".join(x) for x in temp]
                if len(set(temp)) == r:
                    data[len(case)].append(list(case))
    return sum([len(v) for v in data.values()])


def solution(relation):
    answer_list = list()
    col = len(relation[0])
    row = len(relation)

    for i in range(1, 1 << col):  # 1 ~ 16 : 전체 경우의 수 -> combination 대신
        for num in answer_list:
            if (num & i) == num:  # answer_list에 i(부분 집합)가 존재하는 경우
                break
        else:
            tmp_set = set()
            for j in range(row):
                tmp = ''
                for k in range(col):
                    if i & (1 << k):  # 원소 포함 여부
                        tmp += str(relation[j][k])
                tmp_set.add(tmp)

            if len(tmp_set) == row:
                answer_list.append(i)

    return len(answer_list)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
