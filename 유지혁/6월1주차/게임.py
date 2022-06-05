#1103 게임
# 보드판 위의 숫자만큼이동하고, H에 도착하면 게임 종료
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(cx, cy):
    global state

    #종료, 반환조건 
    if not(0 <= cx < N and 0 <= cy < M) or arr[cx][cy] == 'H':
        return 0

    if visited[cx][cy] == True:
        return -1

    if dp[cx][cy] != -1:
        return dp[cx][ny]

    #다음 위치 탐색 
    visited[cx][cy] = True
    for i in range(4):
        nx = cx + (dx[i] * int(arr[cx][cy]))
        ny = cy + (dy[i] * int(arr[cx][cy]))
        dp[cx][cy] = max(dp[cx][cy],dfs(nx,ny) + 1)

    visited[cx][cy] = False
    return dp[cx][cy]
            
if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]    
    dp =[ [-1 for _ in range(M)] for _ in range(N)]
    visited = [ [False for _ in range(M)] for _ in range(N)]
    print(dfs(0,0))
