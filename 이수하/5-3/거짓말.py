'''
집합
'''

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
truth = set(input().split()[1:])

participant = []

# 참가자
for i in range(M):
    participant.append(set(input().split()[1:]))

# 모든 파티 확인, 교집합을 찾아 진실을 아는 참가자 확인
for i in range(M):
    for party in participant:
        if truth & party:
            truth = truth.union(party)
            print(truth)

# 접점이 없는 파티만 체크
count = 0
for party in participant:
    if truth & party:
        continue
    count += 1
    
print(count)
