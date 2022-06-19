"""
dp를 활용하여 구하되, 여러번 루프를 반복해야하기 때문에 문제 발생 가능

neotowheret
4
one
two
three
there
"""

S = input()
N = int(input())
words = []
D = {}
for n in range(N):
    word = input()
    words.append(word)
    D[word] = {}
    for i in word:
        if i in D[word]:
            D[word][i] += 1
        else:
            D[word][i] = 1
words.sort(key=lambda x: len(x))

INF = 1000000
dp = [INF for i in range(len(S))] + [0]

for e in range(len(S)):
    targetDic = {}
    for s in range(e, -1, -1):
        target = S[s:e+1]
        if S[s] not in targetDic:
            targetDic[S[s]] = 1
        else:
            targetDic[S[s]] += 1

        for i in range(N):
            word = words[i]
            # 철자 검증
            if D[word] != targetDic:
                continue
            # 몇이나 차이나는지
            count = 0
            for j in range(len(word)):
                if target[j] != word[j]:
                    count += 1
            dp[e] = min(dp[e], dp[s-1] + count)
if dp[len(S)-1] == INF:
    print(-1)
else:
    print(dp[len(S)-1])
