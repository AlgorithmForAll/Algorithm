from collections import deque
N = int(input())
final = list(map(int, input().split()))


def calc(cards, K):
    # 첫번째 단계
    _cards = deque([])
    for i in range(2**K):
        _cards.appendleft(cards.pop())
    # 이후
    for i in range(2, K+2):
        _cards2 = deque([])
        for j in range(2**(K-i+1)):  # 카드를 앞으로 뺀다.
            _cards2.appendleft(_cards.pop())
        for _ in range(len(_cards)):
            cards.appendleft(_cards.pop())
        _cards = _cards2
    for i in range(len(_cards)):
        cards.appendleft(_cards.pop())


for i in range(1, N+1):
    if 2**i > N:
        break
    else:
        K = i
# 경우의 수 구하기
for i in range(1, K+1):
    for j in range(1, K+1):
        tmp = deque([c for c in range(1, N+1)])
        calc(tmp, i)
        calc(tmp, j)
        if list(tmp) == final:
            print(i, j)
            exit()
