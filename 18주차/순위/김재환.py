"""
dp[i][j] == INF가 들어가야하는 이유는 머지?
"""


def solution(n, results):
    answer = 0
    # init
    INF = 0
    dp = [[INF for i in range(n)] for i in range(n)]
    for re in results:
        a, b = re
        dp[a-1][b-1] = 1
        dp[b-1][a-1] = -1
    print(dp)
    # floid => KIJ
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] == INF and dp[i][k] == dp[k][j]:  # 서열 명확
                    dp[i][j] = dp[i][k]
                    dp[j][i] = -dp[i][k]
    # final
    for l in dp:
        cnt = 0
        for k in l:
            if k == 0:
                cnt += 1
        if cnt <= 1:
            answer += 1
    return answer


"""
def solution(n, results):
    inf = 100
    dp = [[inf for i in range(n+1)] for i in range(n+1)]
    for item in results:
        a,b = item
        dp[a][b] = 1
        dp[b][a] = -1
    
    # 플로이드는 키즈~ k i j
    count = 1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][j] == inf:
                    if dp[i][k] == 1 and dp[k][j] == 1:
                        dp[i][j] = 1
                    if dp[i][k] == -1 and dp[k][j] == -1:
                        dp[i][j] = -1
    print(dp)
    flag = True
    count=0
    for i in range(1,n+1):
        flag = True
        for j in range(1,n+1):
            if i == j:#자기 자신인경우를 제외
                continue
            if dp[i][j] == inf:
                flag = False
                break
        if flag == True:
            count+=1
                
    return count"""
