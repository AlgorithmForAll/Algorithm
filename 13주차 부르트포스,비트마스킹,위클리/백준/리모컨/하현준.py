"""
리모컨
https://www.acmicpc.net/problem/1107
"""
n = int(input())
m = int(input())
data = list(map(int, input().split()))
data = set([i for i in range(10) if i not in data])

answer = abs(100 - n)

for num in range(10 ** 6):  # 최대 범위를 구하는게 포인트
    for i in range(len(str(num))):
        if int(str(num)[i]) not in data:
            break
    else:
        answer = min(answer, abs(n - num) + len(str(num)))

print(answer)
