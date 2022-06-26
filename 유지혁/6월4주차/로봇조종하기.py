#2169 로봇 조종하기
# DP 

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # dp[i][j] :(1,1)에서 (i,j)에 도착했을 때 최대 가치의 합
    # left[i][j] : 위에서 내려와 오른쪽으로 가며 (i,j)에 도착했을 때 최대 가치의 합
    # right[i][j] : 위에서 내려와 왼쪽으로 가며 (i,j)에 도착했을 때 최대 가치의 합
    dp = [[-100000000] * M for _ in range(N)]
    left = [[-100000000] * M for _ in range(N)]
    right = [[-100000000] * M for _ in range(N)]

    # 첫번째 줄은 무조건 왼 -> 오 밖에 없음
    dp[0][0] = arr[0][0]
    for j in range(1,M):
        dp[0][j] = dp[0][j-1] + arr[0][j]

    # 두 번째 줄 탐색
    for i in range(1,N):
        #가장 마지막 끝은 위에서 내려오는 방법밖에 없음 
        left[i][0] = dp[i-1][0] + arr[i][0]
        right[i][M-1] = dp[i-1][M-1]+ arr[i][M-1]
        
        #left[i][j] : 위에서 오는 방법(dp[i-1][j]), 왼쪽에서 오는 방법(left[i][j-1]) 중 큰 값 + arr[i][j]
        for j in range(1,M):
            left[i][j] = max(dp[i-1][j], left[i][j-1]) + arr[i][j]

        #right[i][j] : 위에서 오는 방법(dp[i-1][j]), 오른쪽에서 오는 방법(right[i][j+1]) 중 큰 값 + arr[i][j]
        for j in range(M-2,-1,-1):
            right[i][j] = max(dp[i-1][j], right[i][j+1]) + arr[i][j]

        #dp[i][j] : left[i][j]와 right[i][j] 중 큰 값 
        for j in range(M):
            dp[i][j] = max(right[i][j], left[i][j])

    print(dp[N-1][M-1])
    
