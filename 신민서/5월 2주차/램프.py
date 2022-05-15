"""
출처: https://kominjae.tistory.com/53
"""

N, M = map(int,input().split())
MAPS = []
for i in range(N):
    line = list(map(int, list(input())))
    MAPS.append(line)
K = int(input())
cnt = [0]*N
if K%2: #K가 짝수인 경우
    for i in range(N):
        zero_cnt = MAPS[i].count(0)
        if zero_cnt%2 and zero_cnt <= K: #0의 개수가 짝수이고 K보다 작거나 같으면 모두 킬 수 있다.
            for j in range(N):
                if MAPS[i] == MAPS[j]: #예를들어 MAPS[i]가 010이고 MAPS[j]가 010, K가 2인 경우 두개 다 킬 수 있다.
                    cnt[i] += 1
else:
    for i in range(N):
        zero_cnt = MAPS[i].count(0)
        if not zero_cnt%2 and zero_cnt <= K:
            for j in range(N):
                if MAPS[i] == MAPS[j]:
                    cnt[i] += 1
print(max(cnt))