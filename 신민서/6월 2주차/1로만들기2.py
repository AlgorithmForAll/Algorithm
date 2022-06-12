"""
출처:
https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-12852%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DP
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
q.append([n])
ans = []

while q:
    a = q.popleft() #큐에 정답을 거꾸로 해서 쌓아올리고 답을 출력할 때 다시 뒤집어 출력하는 방식
    x = a[0]
    if x == 1:
        ans = a #x가 1이면 그 a를 그대로 답으로 반환한다.
        break

    if x % 3 == 0:
        q.append([x // 3] + a)

    if x % 2 == 0:
        q.append([x // 2] + a)

    q.append([x - 1] + a) #a가 [5, 10]이고 x가 5라면, [5, 10]이 나오고 [4, 5, 10]이 대신 들어가게 된다.

print(len(ans) - 1) #연산은 숫자들 개수 - 1이기 때문에 len(ans)-1.
print(*ans[::-1]) #ans 반대로 출력.