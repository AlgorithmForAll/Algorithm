def solution(land):
    D = [[0 for _ in range(4)] for __ in range(len(land))]
    D[0][0] = land[0][0]
    D[0][1] = land[0][1]
    D[0][2] = land[0][2]
    D[0][3] = land[0][3]
    for i in range(1, len(land)):
        D[i][0] = max(D[i-1][1], D[i-1][2], D[i-1][3]) + land[i][0]
        D[i][1] = max(D[i-1][0], D[i-1][2], D[i-1][3]) + land[i][1]
        D[i][2] = max(D[i-1][0], D[i-1][1], D[i-1][3]) + land[i][2]
        D[i][3] = max(D[i-1][0], D[i-1][1], D[i-1][2]) + land[i][3]
    return max(D[len(land)-1])