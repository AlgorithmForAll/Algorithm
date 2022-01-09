def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    pan = [[INF] * n for _ in range(n)]
    for i in range(n):
        pan[i][i] = 0
    for f in fares:
        pan[f[0]-1][f[1]-1] = f[2]
        pan[f[1]-1][f[0]-1] = f[2]
    for t in range(n):
        for i in range(n):
            for j in range(i, n):
                if i!=j:
                    pan[i][j] = min(pan[i][j], pan[i][t]+pan[t][j])
                    pan[j][i] = pan[i][j]
    answer = INF
    for t in range(n):
        temp = pan[s-1][t] + pan[t][a-1] + pan[t][b-1]
        answer = min(answer, temp)
    return answer