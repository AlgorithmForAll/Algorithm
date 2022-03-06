"""
외벽 점검
https://programmers.co.kr/learn/courses/30/lessons/60062
"""
from itertools import permutations


def solution(n, weak, dist):
    answer = float('inf')
    wlen = len(weak)
    dist.sort(reverse=True)
    new_weak = weak + [w + n for w in weak]
    for fcase in permutations(dist):
        for start in range(wlen):
            fcount = 0
            data = set()

            for friend in fcase:
                fcount +=1
                wpoint = new_weak[start]
                for i in range(start, len(new_weak)):
                    if wpoint + friend >= new_weak[i]:
                        data.add(new_weak[i] % n)
                    else:
                        start = i
                        break

                if len(data) == wlen:
                    answer = min(answer, fcount)
                    break

    return answer if answer != float('inf') else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), 2)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]), 1)
print(solution(12, [10, 0], [1, 2]), 1)
print(solution(200, [0, 100], [1, 1]), 2)
