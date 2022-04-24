"""
참고사이트 : https://kbw1101.tistory.com/29
브루트포스로 구현하다가 시간초과가 나서 이분탐색으로 구현하는 방법을 참고했다.
"""

n = int(input())
k = int(input())
left = 1
right = n*n
ans = 0
while left <= right:
    mid = (left + right) // 2
    result = 0
    for i in range(1, n+1):
        result += min(n, mid//i)
    if result >= k: # 찾고자 하는 숫자가 배열에 2개 이상이 있는 경우가 있어서 result==k인 경우만 생각해서는 안된다.
        ans = mid
        right = mid - 1
    elif result < k:
        left = mid + 1
print(ans)
