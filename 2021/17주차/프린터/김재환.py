from collections import deque


def solution(priorities, location):
    answer = 0
    pl = deque(list(reversed(sorted(priorities))))
    d = []

    for p in range(len(priorities)):
        d.append([p, priorities[p]])

    d = deque(d)

    cnt = 0
    print(d)
    while d:
        i, p = d.popleft()
        if p == pl[0]:
            cnt += 1
            if i == location:
                print(i, p)
                return cnt
            pl.popleft()
            print([i, p], cnt)
        else:
            d.append([i, p])
        print(d)
    return answer


tmp = solution([2, 1, 3, 2]	, 2)
#tmp = solution([1, 1, 9, 1, 1, 1]		, 0)
print(tmp)
