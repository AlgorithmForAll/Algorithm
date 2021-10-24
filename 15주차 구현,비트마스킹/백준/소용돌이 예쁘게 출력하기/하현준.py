"""
소용돌이 예쁘게 출력하기
https://www.acmicpc.net/problem/1022
"""
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
r1, c1, r2, c2 = map(int, input().split())
row, col = (r2 - r1 + 1), (c2 - c1 + 1)
data = [[0 for _ in range(col)] for _ in range(row)]

size = row * col
dist, num = 1, 1
count, kcount = 0, 0
x, y, k = 0, 0, 0
max_len = -1

if r1 <= x <= r2 and c1 <= y <= c2:
    data[x - r1][y - c1] = 1
    count += 1

while count < size:
    for _ in range(dist):
        kcount += 1
        num += 1
        x += dx[k % 4]
        y += dy[k % 4]

        if r1 <= x <= r2 and c1 <= y <= c2:
            max_len = max(max_len, len(str(num)))
            data[x - r1][y - c1] = num
            count += 1
            if count == size:
                break
        if kcount == dist:
            k += 1
            kcount = 0
            if k % 2 == 0:
                dist += 1

for i in range(row):
    for j in range(col):
        print(f"{data[i][j]:{max_len}}", end=" ")
    print()
