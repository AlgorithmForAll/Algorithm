"""
출처:
https://hbj0209.tistory.com/143
"""

N, S = map(int, input().split())
nums = list(map(int, input().split()))
i, j = 0, 0 #투포인터 알고리즘. i가 left, j가 right
s = nums[0]
ans = 100001

while True:
    if s >= S: #S보다 s가 크면
        s -= nums[i] #i위치에 있는 숫자 빼준다.
        ans = min(ans, j - i + 1) #현재 답 길이보다 지금 길이가 더 짧으면 그걸로 업데이트.
        i += 1 #i(left) 는 1만큼 증가
    else:
        j += 1 #s보다 작으면 숫자를 하나 늘려줘야하기 때문에 j(right)를 1 증가.
        if j == N: #j가 끝에 도달하면 i를 옮겨봤자 계속 S보다 작을 것이기 때문에 그냥 break
            break
        s += nums[j] #그렇지 않으면 j위치의 숫자를 s에 더해준다.

print(0) if ans == 100001 else print(ans)
