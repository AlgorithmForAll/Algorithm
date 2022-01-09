"""
순위
https://programmers.co.kr/learn/courses/30/lessons/49191
참고 : https://velog.io/@narastro/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-Python
"""
from collections import defaultdict


def solution(n, results):
    answer = 0
    before = defaultdict(set)
    after = defaultdict(set)
    for a, b in results:
        before[a].add(b)
        after[b].add(a)
    for i in range(1, n+1):
        for bi in before[i]:
            # i 보다 뒤에 있는 애들 -> i 앞에 있는 애들보다 당연히 뒤에 있음
            after[bi].update(after[i])
        for ai in after[i]:
            before[ai].update(before[i])
    for i in range(1, n+1):
        if len(after[i]) + len(before[i]) == n-1:
            answer +=1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5, 6], [6, 7]]), 4)
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]), 6)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(3, [[1, 2], [1, 3]]), 1)
print(solution(6, [[1, 6], [2, 6], [3, 6], [4, 6]]), 0)
print(solution(8, [[1, 2], [3, 4], [5, 6], [7, 8]]), 0)
print(solution(9, [[1, 2], [1, 3], [1, 4], [
      1, 5], [6, 1], [7, 1], [8, 1], [9, 1]]), 1)
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [2, 4], [2, 6]]), 6)
print(solution(4, [[4, 3], [4, 2], [3, 2], [3, 1], [4, 1], [2, 1]]), 4)
print(solution(3, [[3, 2], [3, 1]]), 1)
print(solution(4, [[1, 2], [1, 3], [3, 4]]), 1)

