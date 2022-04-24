"""
이중우선순위큐
https://programmers.co.kr/learn/courses/30/lessons/42628
"""
import heapq


def solution(operations):
    minh = []
    maxh = []
    answer = []
    deleted = []
    count = 0
    for op in operations:
        otype, num = op.split()
        num = int(num)

        if otype == "I":
            count += 1
            heapq.heappush(minh, num)
            heapq.heappush(maxh, -num)

        elif otype == "D" and count > 0:
            count -= 1
            if num == 1:
                deleted.append(-heapq.heappop(maxh))
            elif num == -1:
                deleted.append(heapq.heappop(minh))

    if count == 0:
        return [0, 0]

    while maxh:
        now = -heapq.heappop(maxh)
        if now not in deleted:
            answer.append(now)
            break

    while minh:
        now = heapq.heappop(minh)
        if now not in deleted:
            answer.append(now)
            break

    return answer


print(solution(["I 16", "D 1"]), [0, 0])
print(solution(["I 7", "I 5", "I -5", "D -1"]), [7, 5])
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]), [0, 0])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]), [333, -45])
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]), [6, 5])
print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]),[3,3])