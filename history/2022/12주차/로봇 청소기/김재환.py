"""
1. 왼쪽탐색 o -> 왼쪽방향 -> 1칸 이동
2. 왼쪽탐색 x-> 왼쪽방향
3. 4방향 탐색o -> 뒤로 1칸
4. 4방향 탐색o + 뒤가 벽 -> 작동 멈춤 == 종료 시그널

0북 1동 2남 3서

좌표, 방향, 어디 방향 탐색했는지
"""

N, M = map(int, input().split())
y, x, d = map(int, input().split())
Map = []
for i in range(N):
    tmp = list(map(int, input().split()))
    Map.append(tmp)


def turnLeft(d):  # 3->2->1->0 ->3..... d+3%3 = 왼쪽방향
    d -= 1
    if d == -1:
        d = 3
    return d


def turnReverse(d):  # 3->2->1->0 ->3..... d+3%3 = 왼쪽방향
    return (d+2) % 4


visited = [[0 for i in range(M)] for i in range(N)]
dvisited = [[[0, 0, 0, 0] for i in range(M)] for i in range(N)]
visited[y][x] = 1
count = 1
D = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}  # 북, 동, 남, 서


while True:
    y, x, d
    flag = 0
    ny, nx = 0, 0
    for _ in range(4):
        d = turnLeft(d)
        dy, dx = D[d]
        ny, nx = y + dy, x + dx
        if Map[ny][nx] == 0 and visited[ny][nx] == 0:  # 갈 수 있는경우
            flag = 1
            break
    if flag == 1:  # 갈수 있는 경우
        visited[ny][nx] = 1
        count += 1
        y, x = ny, nx
    else:  # 4방향 모두 갈 수 없는경우
        rd = turnReverse(d)
        dy, dx = D[rd]
        ny, nx = y + dy, x + dx
        if Map[ny][nx] == 1:  # 뒤도 벽이다
            break
        else:  # 뒤가 벽이 아니다
            if visited[ny][nx] != 1:
                visited[ny][nx] = 1
                count += 1
            y, x = ny, nx
print(count)
