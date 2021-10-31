"""
고층 건물
https://www.acmicpc.net/problem/1027
참고
"""

n = int(input())
data = list(map(int, input().split()))
count_data = [0] * n

for i in range(n):
    temp = -99999999999
    for j in range(i + 1, n):
        grad = (data[j] - data[i]) / (j - i)  # grad : 현재 건물 j와의 기울기
        if grad > temp:  # temp : 이전 건물과의 기울기
            temp = grad
            # 건물 i와 j는 서로 볼 수 있는 상태 -> 각각 +1
            count_data[i] += 1
            count_data[j] += 1

print(max(count_data))
