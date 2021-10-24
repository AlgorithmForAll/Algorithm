"""
숫자 정사각형
https://www.acmicpc.net/problem/1051
"""
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        for dist in range(min(n, m)):
            try:
                val = []
                for k in range(4):
                    val.append(data[i+dx[k]*dist][j+dy[k]*dist])
                if min(val) == max(val):
                    result = max(result, dist+1)
            except IndexError:
                pass

print(result*result)