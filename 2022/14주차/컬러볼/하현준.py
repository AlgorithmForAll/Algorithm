"""
컬러볼 
https://www.acmicpc.net/problem/10800
참고 : https://jjangsungwon.tistory.com/123
누적합 연습하자...
"""
from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
ball = [[i] + list(map(int, input().split())) for i in range(n)]
ball.sort(key=lambda x: x[2])

answer = defaultdict(int)
ball_size_sum = defaultdict(int)  # 색깔 별 공의 크기 누적합

total = 0  # 총합
j = 0
for i in range(n):
    num, color, size = ball[i]
    while ball[j][2] < size:  # 크기가 작을 때까지 수행
        total += ball[j][2]
        ball_size_sum[ball[j][1]] += ball[j][2]
        j += 1
    answer[num] = total - ball_size_sum[color]  # 총합 - 현재 색깔 공 누적합

for i in range(n):
    print(answer[i])
