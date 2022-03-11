"""
n^2 배열 자르기
https://programmers.co.kr/learn/courses/30/lessons/87390
"""


def solution(n, left, right):
    print("-" * 40)
    left = int(left)
    right = int(right)
    answer = []
    x1 = left // n + 1 if left / n >= left // n else left // n
    x2 = right // n + 1 if right / n >= right // n else right // n
    start = left % n
    for i in range(x1, x2 + 1):
        answer.append([i for _ in range(i)] + [i + j + 1 for j in range(n - i)])
    answer = sum(answer, [])
    return answer[start:start + right - left + 1]


print(solution(3, 2, 5), [3, 2, 2, 3])
print(solution(4, 7, 14), [4, 3, 3, 3, 4, 4, 4, 4])
print(solution(1, 0, 0), [1])
print(solution(2, 2, 2), [1])
