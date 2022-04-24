"""
단어를 비트 마스킹으로 바꾸고 연산하면 엄청 간단히 비교가 가능하다.
꼬박 하루 걸렸는데 비트마스킹을 공부하고 이해하기에 아주 좋은 문제였던거 같다.
"""
from itertools import combinations
N, K = map(int, input().split())
padd = ['a', 'n', 't', 'i', 'c']
words = []
ch = set([])
for _ in range(N):
    bit = 0
    tmp = input()[4:-4]
    for i in range(len(tmp)):
        bit = bit | (1 << (ord(tmp[i])-96))
        if tmp[i] not in padd:
            ch.add(tmp[i])
    words.append(bit)

if K < 5:
    print(0)
    exit()
# 조합만들기
vis = 0
for i in padd:
    vis = vis | (1 << (ord(i)-96))

K = K-5
if len(ch) < K:
    K = len(ch)
combs = list(combinations(ch, K))

big = 0
for comb in combs:
    visited = vis
    for com in comb:
        visited = visited | (1 << (ord(com)-96))
    count = 0
    for word in words:
        if (word & visited) == word:
            count += 1
    big = max(big, count)
print(big)
