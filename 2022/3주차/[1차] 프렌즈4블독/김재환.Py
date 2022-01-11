def solution(m, n, board):
    answer = 0

    # 전처리
    Map = []
    for b in board:
        Map.append(list(b))
    while True:
        # 반복하면서 찾기
        s = findBlock(m, n, Map)
        if len(s) == 0:
            break
        answer += len(s)
        for t in s:
            i, j = t
            Map[i][j] = 0
        # 블록 내리기
        downBlock(m, n, Map)
        s = findBlock(m, n, Map)

    return answer


def downBlock(m, n, Map):
    for j in range(n):  # 폭
        for i in range(m-1, -1, -1):  # 높이
            if Map[i][j] != 0:
                continue
            # Map[i][j] == 0 이면 데이터 가져오기
            fi = i-1
            while 0 <= fi:
                if Map[fi][j] != 0:
                    Map[i][j] = Map[fi][j]
                    Map[fi][j] = 0
                    break
                else:
                    fi -= 1


def findBlock(m, n, Map):  # 높이, 폭
    s = set()
    for i in range(m-1):
        for j in range(n-1):

            if Map[i][j] != 0 and Map[i][j] == Map[i][j+1] and Map[i][j] == Map[i+1][j] and Map[i][j] == Map[i+1][j+1]:
                s.add((i, j))
                s.add((i, j+1))
                s.add((i+1, j))
                s.add((i+1, j+1))
    return s
