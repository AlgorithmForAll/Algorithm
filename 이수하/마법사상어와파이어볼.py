import sys
input = sys.stdin.readline


# 파이어볼 이동하기
def moveFireball():
    while fireball:
        r, c, m, s, d = fireball.pop(0)
        
        nx = (r + dx[d]*s)%N
        ny = (c + dy[d]*s)%N
        
        map[nx][ny].append([m, s, d])
        
# 2개 이상 파이어볼 찾기
def findFireball():
    for i in range(N):
        for j in range(N):
            if len(map[i][j]) > 1:
                actionFireball(i, j)
            if len(map[i][j]) == 1:
                fireball.append([i, j]+map[i][j].pop(0))

# 파이어볼 깨지기    
def actionFireball(i, j):
    _m, _s, _odd, _even = 0, 0, 0, 0

    length = len(map[i][j])
    while map[i][j]:
        m, s, d = map[i][j].pop(0)
        _m += m
        _s += s
        if d % 2 == 0:
            _odd += 1
        else:
            _even += 1
    
    _m = _m//5
    _s = _s//length
    
    # 질량이 0 아닐 때 ( 0이면 사라짐 )
    if _m:
        # 파이어볼 모두 짝수 또는 홀수일 때
        if _odd == length or _even == length:
            for _ in range(0, 8, 2):
                fireball.append([i, j, _m, _s, _])
        else:
            for _ in range(1, 9, 2):
                fireball.append([i, j, _m, _s, _])
        

N, M, K = map(int, input().split())

fireball = []
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1, m, s, d])
   
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

map = [[[] for i in range(N)] for j in range(N)]

for i in range(K):
    moveFireball()
    findFireball()

# 남은 파이어볼 질량 합 출력
sum = 0
for i in fireball:
    sum += i[2]
    
print(sum)