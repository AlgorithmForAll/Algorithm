"""
https://www.acmicpc.net/problem/1036
가중치-> z로 변환 했을 때 얼마만큼의 이득인지 체크
"""
from collections import defaultdict
import sys

sys.stdin = open("../input.txt")


def convert(num):
    result = ''
    while num != 0:
        num, mod = divmod(num, 36)
        result += str(rev_data[mod])
    return result[::-1]


data = dict((chr(i), i - ord('A') + 10) for i in range(ord('A'), ord('Z') + 1))
for i in range(10):
    data[str(i)] = i
rev_data = dict((v, k) for k, v in data.items())

for _ in range(100):
    nums_data = defaultdict(int)

    n = int(input())
    for _ in range(n):
        num = input()
        size = len(num)
        for idx, val in enumerate(num):
            nums_data[val] += 36 ** (size - 1 - idx)
    k = int(input())

    nums_data = list(nums_data.items())
    nums_data.sort(key=lambda x: -(x[1] * abs(35 - data[x[0]])))
    result = 0
    for word, val in nums_data:
        if k > 0:
            k -= 1
            result += 35 * val
        else:
            result += data[word] * val
    result = convert(result)
    print(result if result else 0)
