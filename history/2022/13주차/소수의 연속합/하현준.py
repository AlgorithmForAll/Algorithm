"""
소수의 연속합
https://www.acmicpc.net/problem/1644
"""
import sys

sys.stdin = open("../input.txt")


def get_primes(num):
    check = [True] * num

    m = int(num ** 0.5)
    for x in range(2, m + 1):
        if check[x]:  # x가 소수인 경우
            for j in range(x + x, num, x):  # x이후의 x의 배수들은 모두 false 체크
                check[j] = False

    return [i for i in range(2, num) if check[i] == True]


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    else:
        primes = list(get_primes(n + 1))
        a = 0
        b = 0
        count = 0
        result = primes[0]
        limit = len(primes)
        while a <= b < limit:
            if result < n:
                b += 1
                if b < limit:
                    result += primes[b]
            elif result == n:
                count += 1
                result -= primes[a]
                a += 1
            elif result > n:
                result -= primes[a]
                a += 1

        print(count)
