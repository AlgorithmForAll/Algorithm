"""
점프와 순간 이동
https://programmers.co.kr/learn/courses/30/lessons/12980

"""


def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    return ans


# 세상에나..
def solution2(n):
    return bin(n).count('1')


print(solution(5), 2)
print(solution(6), 2)
print(solution(12), 2)
print(solution(5000), 5)
