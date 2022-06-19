"""
출처:
https://westmino.tistory.com/86
"""

dx = [1,0,-1,0] #우, 하, 좌, 상 네방향 (시계방향)
dy = [0,-1,0,1]

def solution(grid):
    global visited,n,m
    n = len(grid) #행의 개수
    m = len(grid[0]) #열의 개수
    answer = []
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    for sx in range(n):
        for sy in range(m):
            for d in range(4): #모든 sx, sy에서의 상, 하, 좌, 우로 빛을 쏘는 경우를 다 탐색.
                if not visited[sx][sy][d]:
                    rst = simul(sx,sy,d,grid)
                    if rst != 0:
                        answer.append(rst)
    answer.sort()
    return answer

def simul(sx,sy,sd,grid):
    global visited
    x,y,d=sx,sy,sd
    cnt = 0
    visited[sx][sy][sd] = True
    while True:
        x = (x + dx[d]) % n #범위를 벗어나면 반대편으로 오게 하도록 %n, %m을 한다.
        y = (y + dy[d]) % m #예를 들어서 y+dy[d]가 -1이고 m이 4라면, -1%4는 3이여서 반대편 끝쪽으로 가게된다.
        cnt += 1
        if grid[x][y] == 'R':  #우회전
            d = (d+1)%4
        elif grid[x][y] == 'L': #좌회전
            d = (d-1)%4
        if visited[x][y][d]:
            if (x,y,d) == (sx,sy,sd): #방문한 칸이고 시작점과 방향이 같을 경우
                return cnt #사이클 형성. 그대로 cnt 리턴.
            else: #방문한 칸이지만 시작점과 다른 경우 => 제대로된 사이클 형성 x
                return 0 #0 리턴
        visited[x][y][d] = True