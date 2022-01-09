import copy


def rotated(key):
    n = len(key)
    m = len(key[0]
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result


def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    pan = [[0 for _ in range(n * 3)] for __ in range(n * 3)]  # key를 순회시킬 길이까지 포함해서 pan을 만들어준다.
    for i in range(0, n):
        for j in range(0, n):
            pan[i + n][j + n] = lock[i][j]  # pan에 lock 배치
    # print(pan)
    ppan = copy.deepcopy(pan)
    for k in range(4):
        for i in range(n - m + 1, 2 * n):
            for j in range(n - m + 1, 2 * n):
                for ii in range(0, m):
                    for jj in range(0, m):
                        ppan[i + ii][j + jj] += key[ii][jj]
                torf = True
                for ii in range(n, n * 2):
                    for jj in range(n, n * 2):
                        if ppan[ii][jj] == 0 or ppan[ii][jj] == 2:
                            torf = False
                            break
                ppan = copy.deepcopy(pan)
                if torf == True:
                    answer = True
                    break
        if answer == True:
            break
        key = rotated(key)
    return answer