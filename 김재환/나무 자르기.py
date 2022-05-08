"""
이분탐색 냄새 난다.
"""

N, M = map(int, input().split())
ts = list(map(int, input().split()))

L = 0
R = max(ts)
F = 0
while L <= R:
    Mid = int((L+R)//2)
    getTs = 0
    for t in ts:
        if t > Mid:
            getTs += t - Mid
            if getTs > M:
                break

    if M <= getTs:
        L = Mid+1
        F = Mid
    else:
        R = Mid-1
print(F)
