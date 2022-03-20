from collections import deque


def isVertical(robot):
    if robot[0][0] == robot[1][0]:  # 같은 y값은 수직
        return True
    else:
        return False


def BFS(M):

    # 양방향 이동
    dy = [-1, 1, 0, 0]  # 상하좌우
    dx = [0, 0, -1, 1]
    # 회전
    visited = [[0 for i in range(len(M))] for i in range(len(M))]

    q = deque([[0, 0], [0, 1]])
    count = 0
    while q:
        count += 1
        for _ in range(len(q)):
            robot = q.popleft()
            # 4 방향 이동
            for j in range(4):
                _robot = []
                for i in range(2):
                    ny = robot[i][0] + dy[j]
                    nx = robot[i][1] + dx[j]
                    if (0 <= ny < N) and (0 <= nx < N) and M[ny][nx] == 1:
                        _robot.append([yn, nx])
                    else:
                        break
                if len(_robot) != 2:
                    continue
                # 방문 검증  두 칸중 하나라도 0이면 가능, 둘다 1이면 의미 없음
                if visited[_robot[0][0]][_robot[0][1]] == 0 or visited[_robot[1][0]][_robot[1][1]] == 0:
                    q.append(sort(_robot))
            # 회전하는 경우
            if isVertical(robot):  # 수직
                # 위가 중심
                # 왼쪽 회전()
                if M[robot[0][0]][robot[0][1]-1]
                # 오른쪽 회전
                # 아래가 중심
                # 왼쪽 회전
                # 오른쪽 회전
            else:  # 수평


def solution(board):
    answer = 0
    return answer
