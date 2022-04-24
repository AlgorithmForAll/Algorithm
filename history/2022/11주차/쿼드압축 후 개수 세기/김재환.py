def check(Map, y, x, N, answer):
    start = Map[y][x]
    if N == 1:
        if start == 0:
            answer[0] += 1
        else:
            answer[1] += 1
        return
    flag = 0
    count = 0
    for i in range(y, y+N):
        for j in range(x, x+N):
            if Map[i][j] == start:
                count += 1
            else:
                flag = -1
                break
        if flag == -1:
            break
    if flag == -1:  # 분할 필요
        check(Map, y, x, N//2, answer)  # 1사분면
        check(Map, y, x+N//2, N//2, answer)  # 2사분면
        check(Map, y+N//2, x, N//2, answer)  # 3사분면
        check(Map, y+N//2, x+N//2, N//2, answer)  # 4사분면
    else:
        if start == 0:
            answer[0] += 1
        else:
            answer[1] += 1


def solution(arr):
    answer = [0, 0]
    N = len(arr)
    check(arr, 0, 0, N, answer)
    return answer
