import heapq
def solution(operations):
    answer = []
    q = []
    for s in operations:
        s1, num = map(str, s.split())
        num = int(num)
        if s1 == "I" :
            q.append(num)
        elif s1 == "D" :
            if len(q) == 0:
                continue
            elif num == 1 :
                heapq._heapify_max(q)
                heapq.heappop(q)
            elif num == -1 :
                heapq.heapify(q)
                heapq.heappop(q)
    if len(q) == 0:
        answer.append(0)
        answer.append(0)
    else:
        heapq._heapify_max(q)
        answer.append(q[0])
        heapq.heapify(q)
        answer.append(q[0])
    return answer