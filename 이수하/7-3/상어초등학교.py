from heapq import heappush, heappop

# 만족도 0이면 0, 1이면 1, 2면 10, 3이면 100, 4면 1000
def satisfied() :
    result = 0
    for r in range(n) :
        for c in range(n) :
            if not board[r][c] :
                continue
            cnt = 0
            for d in range(4) :
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < n and 0 <= nc < n) :
                    continue
                if board[nr][nc] in likeinfo[board[r][c]] : # 좋아하는 학생 인접한 칸에 있으면
                    cnt += 1
            if cnt : # 10의 -1승이 더해지는 것을 방지
                result += 10 ** (cnt - 1)
    return result

def drawIdx(idx) :
    priorityQueue = [] # 최대 힙 사용 (우선순위 큐로 활용)
    for r in range(n) :
        for c in range(n) :
            if board[r][c] :
                continue
            likeCnt, blankCnt = 0, 0
            for d in range(4) :
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < n and 0 <= nc < n) :
                    continue
                if board[nr][nc] in likeinfo[idx] : # 좋아하는 학생 Set에 있으면
                    likeCnt += 1
                if not board[nr][nc] : # 빈 공간이면
                    blankCnt += 1
            # 최대 힙에 삽입 (우선순위)
            heappush(priorityQueue, (-likeCnt, -blankCnt, r, c))
    like, blank, r, c = heappop(priorityQueue) # 가장 높은 우선순위의 값 뽑은 정보
    board[r][c] = idx

n = int(input())
board = [[0] * n for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

likeinfo = dict() # {학생 번호 : 좋아하는 학생 Set}
for _ in range(n ** 2) :
    info = list(map(int, input().split()))
    likeinfo[info[0]] = set(info[1:])

# 주어진 순서대로 학생 자리 배치
for idx in likeinfo.keys() :
    drawIdx(idx)

# 만족도 조사 결과 출력
print(satisfied())