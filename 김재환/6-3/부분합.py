"""
투포인터로 구하기
"""

N, S = map(int, input().split())
M = list(map(int, input().split()))

L = 0
R = 0
INF = 100000
answer = INF
total = M[L]
# LR
#  5 1 3 5 10 7 4 9 2 8

#  L       R
#  5 1 3 5 10 7 4 9 2 8

#        L R
#  5 1 3 5 10 7 4 9 2 8

#        L    R
#  5 1 3 5 10 7 4 9 2 8

while R < len(M):
    # 합이 성립하는지 판별
    if total < S:  # 만족하지 않으므로 R을 더한다.
        R += 1
        if R >= len(M):  # 투포인터를 종료하기 위한 조건문
            break
        total += M[R]
    else:  # 만족하므로 수를 갱신하고 L을 더한다.
        answer = min(answer, R-L + 1)  # 그 합이 S 이상이면서 가장 짧은것으로 업데이트
        total -= M[L]
        L += 1

if INF == answer:
    print(0)
else:
    print(answer)
