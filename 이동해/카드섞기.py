n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

target = [0, 1, 2] * (n // 3)
init = p
cnt = 0

while True:
    if p == target:
        print(cnt)
        break

    temp = [0] * n
    for i in range(n):
        temp[s[i]] = p[i]
    cnt += 1
    p = temp
    
    # 섞은 카드가 초기값과 같아지면 -1 출력
    if p == init:
        print(-1)
        break
