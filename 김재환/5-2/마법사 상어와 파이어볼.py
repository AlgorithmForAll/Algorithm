"""
각 파이어볼은 d방향으로 s칸 이동. 이도웆ㅇ에 여러 파이어볼 가능
2개 이상 파이어볼 겹치면
1. 파이어볼 합치기
2. 파이어볼을 4개의 파이어볼로
3. 질량 : 합쳐진질량 합/5, 속력 : 속력합/파이어볼 개수
4. 합치는 파이어볼 방향이 모두 홀수거나 짝수면 [0,2,4], 아니면[1,3,5,7]
{}로 하면 시간초과남
python3 시간초과남
pypy3는 통과.....=> python으로는 어케 풀지?
"""
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

Map = [[[] for i in range(N)] for i in range(N)]
_Map = [[[] for i in range(N)] for i in range(N)]
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    Map[r-1][c-1] = [(m, s, d)]

# for k in range(K):
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def fireballMove(r, c, fireball):
    m, s, d = fireball
    for _ in range(s):
        r += dy[d]
        c += dx[d]
    if r < 0:
        r = int(N - (-r % N))
    if r > N-1:
        r = int(r % N)
    if c < 0:
        c = int(N - (-c % N))
    if c > N-1:
        c = int(c % N)

    _Map[r][c].append((m, s, d))


for k in range(K):
    _Map = [[[] for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(len(Map[i][j])):
                fireballMove(i, j, Map[i][j][z])
    # points 점검 => 겹치는 경우
    for i in range(N):
        for j in range(N):
            fbNum = len(_Map[i][j])
            if fbNum > 1:
                # 파이어볼 합치기
                totalMass = 0
                totalSpeed = 0
                m, s, sd = _Map[i][j][0]
                dirFlag = True
                for _ in range(fbNum):
                    m, s, d = _Map[i][j].pop()
                    totalMass += m
                    totalSpeed += s
                    if (sd % 2) != (d % 2):
                        dirFlag = False
                totalMass = int(totalMass/5)
                totalSpeed = int(totalSpeed/fbNum)

                if dirFlag == True:  # [0,2,4,6]
                    nextDirs = [0, 2, 4, 6]
                else:  # [1,3,5,7]
                    nextDirs = [1, 3, 5, 7]

                if totalMass == 0:
                    continue
                _Map[i][j] = []
                for nextDir in nextDirs:
                    _Map[i][j].append((totalMass, totalSpeed, nextDir))
    Map = _Map
# 최종값 구하기
total = 0
for i in range(N):
    for j in range(N):
        for z in range(len(Map[i][j])):
            total += Map[i][j][z][0]
print(total)
