"""
물병
https://www.acmicpc.net/problem/1052
"""

n, k = map(int, input().split())
answer = 0
data = 1
num, count = 1, n
while True:
    print(f"{num=} {count=} {data:010b}")
    q, r = count // 2, count % 2
    if count <= 1:
        if bin(data).count("1") <= k:
            break
        first = data & (-data)
        answer += first
        count = first
        num = 1
        print(f"{first=} {data:010b}")
        if data & (1 << 0):
            count += 1
        else:
            data |= 1 << 0
        continue

    count = q
    if data & (1 << num):
        count += 1
    if r == 0:
        data &= ~(1 << (num - 1))
    if q > 0:
        data |= (1 << num)
    num += 1

print(answer)
