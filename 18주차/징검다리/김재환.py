
def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks = sorted(rocks)
    # 이분탐색
    L = 1
    R = distance
    H = 0
    while L <= R:
        M = int((L+R)//2)
        print(L, M, R)
        past = 0
        cnt = 0
        for i in range(len(rocks)):
            if rocks[i] - past < M:
                cnt += 1
            else:
                past = rocks[i]
        print(M, cnt)
        if cnt <= n:
            L = M+1
            H = M
        elif cnt > n:  # 부적절함, M을 줄여야함
            R = M-1
    print(M, H)

    return H


#solution(25, [2, 14, 11, 21, 17]	, 2)
