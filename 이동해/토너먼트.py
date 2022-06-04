'''
1. 인덱스로 풀기
2. 토너먼트이기 때문에 무조건 붙게 돼있다.

def solution(n,a,b):
    count = 0
    a, b = a - 1, b - 1
    while a != b:
        count += 1
        a = a // 2
        b = b // 2
    return count

'''


from collections import deque

n, kim, lim = map(int, input().split())

# 지민과 한수를 1로 나머지는 0으로 설정
game = [0] * n
game[kim - 1] = 1
game[lim - 1] = 1

game = deque(game)
round_num = 0
target = False  # 한수를 만났는지 여부 확인

while True:
    round_num += 1

    # 참가자 홀수 여부 확인
    last = False    
    if len(game) % 2 != 0:
        last = True

    # 2명씩 게임
    for _ in range(len(game) // 2):
        gamer_one = game.popleft()
        gamer_two = game.popleft()
        if gamer_one == 1 and gamer_two == 1:
            target = True
            break
        if gamer_one == 1 or gamer_two == 1:
            game.append(1)
        else:
            game.append(0)
    
    # 참가자가 홀수인 경우 마지막 사람 자동진출
    if last:
        game.append(game.popleft())

    if target:
        print(round_num)
        break

