"""
1. 열증가하는 경우
2. 행 증가하는 경우
"""
import math
M, N = map(int, input().split())

numbers = []
for _ in range(M):
    numbers.append(
        list(map(int, list(input()))))

result = -1
for m in range(M):
    for n in range(N):
        for w_m in range(-M, M):
            for w_n in range(-N, N):
                if w_m == 0 and w_n == 0:
                    continue  # 둘다 0이면 무한루프
                step = 0
                x = m
                y = n
                value = ''
                while (0 <= x < M) and (0 <= y < N):
                    value += str(numbers[x][y])
                    step += 1

                    # 제곱수이고, 최댓값 갱신이 가능한지
                    value_int = int("".join(value))
                    value_sqrt = math.sqrt(value_int)
                    value_deci = value_sqrt - int(value_sqrt)
                    if value_deci == 0 and value_int > result:
                        result = value_int
                    x = m + step * w_m
                    y = n + step * w_n
print(result)
