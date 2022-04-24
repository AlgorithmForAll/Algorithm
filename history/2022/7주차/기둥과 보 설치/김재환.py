def checkPill(Map, y, x):
    # 기둥이 바닥에 있거나, 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있거나
    if y == 0 or (Map[y][x-1][1] == 1 or Map[y][x][1] == 1) or Map[y-1][x][0] == 1:
        return True
    else:
        return False


def checkLine(Map, y, x):
    # 보는 한쪽끝 부분이 기둥위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시 연결인경우
    if (Map[y-1][x][0] == 1 or Map[y-1][x+1][0] == 1) or (Map[y][x-1][1] == 1 and Map[y][x+1][1] == 1):
        return True
    else:
        return False


def solution(n, build_frame):
    answer = []
    Map = [[[0, 0] for i in range(n+2)]for i in range(n+2)]  # 기둥,보

    for build in build_frame:
        print(build)
        x, y, a, b = build  # a -> 0:기둥, 1:보 / b -> 0:삭제, 1:설치
        if a == 0:  # 기둥
            if b == 1:  # 설치
                if checkPill(Map, y, x):
                    Map[y][x][0] = 1
            else:
                Map[y][x][0] = 0
                flag = 0
                for i in range(n+1):
                    for j in range(n+1):
                        if Map[i][j][0] == 1:
                            if checkPill(Map, i, j) == False:
                                flag = 1
                        if Map[i][j][1] == 1:
                            if checkLine(Map, i, j) == False:
                                flag = 1
                if flag == 1:
                    Map[y][x][0] = 1

        else:  # 보
            if b == 1:  # 보 설치
                if checkLine(Map, y, x):
                    Map[y][x][1] = 1
            else:
                Map[y][x][1] = 0
                flag = 0
                for i in range(n+1):
                    for j in range(n+1):
                        if Map[i][j][0] == 1:
                            if checkPill(Map, i, j) == False:
                                flag = 1
                        if Map[i][j][1] == 1:
                            if checkLine(Map, i, j) == False:
                                flag = 1
                if flag == 1:
                    Map[y][x][1] = 1
    for i in range(n+1):
        for j in range(n+1):
            if Map[i][j][0] == 1:  # 기둥 존재
                answer.append([j, i, 0])
            if Map[i][j][1] == 1:  # 보 존재
                answer.append([j, i, 1])
    answer.sort()
    print(answer)

    return answer
