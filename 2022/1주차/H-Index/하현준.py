"""
H-Index
https://programmers.co.kr/learn/courses/30/lessons/42747
"""


def lower_bound(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for h in range(n + 1):
        index = lower_bound(citations, h)
        if n - index >= h >= index:
            answer = max(answer, h)
    return answer


print(solution([3, 0, 6, 1, 5]), 3)
