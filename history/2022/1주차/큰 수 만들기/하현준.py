"""
큰 수 만들기
https://programmers.co.kr/learn/courses/30/lessons/42883
"""
from collections import deque


def solution(number, k):
    result = deque([number[0]])
    i = 1
    while i < len(number):
        while result[-1] < number[i]:
            k -= 1
            result.pop()
            if k == 0 or not result:
                break
        if k == 0:
            result.extend(number[i:])
            break
        result.append(number[i])
        i += 1

    if k > 0:
        result = list(result)[:-k]
    return "".join(result)


print(solution("8911", 2), "91")
print(solution("1119", 1), "119")
print(solution("999", 2), "9")
print(solution("1924", 2), "94")
print(solution("1199", 2), "99")
print(solution("8989", 2), "99")
print(solution("8899", 2), "99")
print(solution("9911", 2), "99")
print(solution("1231234", 3), "3234")
print(solution("4177252841", 4), "775841")
print(solution("4177999941", 4), "999941")
print(solution("4177999941", 5), "99994")
print(solution("4177999914", 5), "99994")
print(solution("417799991499119", 8), "9999999")
