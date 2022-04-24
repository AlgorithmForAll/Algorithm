"""
모음 사전
https://programmers.co.kr/learn/courses/30/lessons/84512
"""


def solution(word):
    answer = 0
    for idx, val in enumerate(word):
        answer += data[idx][val]
    return answer

gap = 1
data = dict({4: {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}})
for i in range(3, -1, -1):
    data[i] = dict()
    start = 1
    gap += 5 ** (4 - i)
    for idx, alpha in enumerate(["A", "E", "I", "O", "U"]):
        data[i][alpha] = start
        start += gap


print(solution("AAAAE"), 6)
print(solution("AAAE"), 10)
print(solution("I"), 1563)
print(solution("EIO"), 1189)
