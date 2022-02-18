def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:  # 짝수
            n /= 2
        else:  # 홀수
            n -= 1
            ans += 1
    return ans
