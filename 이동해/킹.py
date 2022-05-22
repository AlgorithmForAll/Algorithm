king, stone, n = input().split()

# 문자를 숫자로 변경
king_x, king_y = ord(king[0]) - 64, int(king[1])
stone_x, stone_y = ord(stone[0]) - 64, int(stone[1])
 

# 명령어로 좌표 이동하는 함수
def movePieces(order, x, y):
    if order == 'R':
        x = x + 1
    elif order == 'L':
        x = x - 1 
    elif order == 'B':
        y = y - 1
    elif order == 'T':
        y = y + 1
    elif order == 'RT':
        x, y = x + 1, y + 1
    elif order == 'LT':
        x, y = x - 1, y + 1
    elif order == 'RB':
        x, y = x + 1, y - 1
    else:
        x, y = x - 1, y - 1
    return x, y

for _ in range(int(n)):
    order = input()
    king_nx, king_ny = movePieces(order, king_x, king_y)
    
    # 돌이 있는 곳으로 이동할 경우
    if (king_nx == stone_x) and (king_ny == stone_y):
        stone_nx, stone_ny = movePieces(order, stone_x, stone_y)
        # 범위 확인
        if (1 <= stone_nx <= 8) and (1 <= stone_ny <= 8):
            stone_x, stone_y = stone_nx, stone_ny
            king_x, king_y = king_nx, king_ny

    # 돌이 없는 곳으로 이동할 경우
    else:
        # 범위 확인
        if (1 <= king_nx <= 8) and (1 <= king_ny <= 8):
            king_x, king_y = king_nx, king_ny

print(chr(king_x + 64) + str(king_y))
print(chr(stone_x + 64) + str(stone_y))


