"""
https://bellog.tistory.com/152

"""


def solution(name):
    answer = 0
    min_move = len(name)-1  # 그냥 오른쪽으로만 다 도는 경우
    next = 0

    for i, char in enumerate(name):
        # 상하 조이스틱 움직임
        answer += min(ord(char) - ord('A'), ord('Z')-ord(char)+1)

        # 좌우 조이스틱 움직임
        next = i+1  # 현재 값의 다음값
        while next < len(name) and name[next] == 'A':  # A가 연속되는 부분까지를 구함
            next += 1
        # i까지 오고 다시 왼쪽으로 넘어가는 경우의 최솟값을 구해서 비교하고 갱신
        min_move = min(min_move, i+i+len(name)-next)
    answer += min_move

    return answer
