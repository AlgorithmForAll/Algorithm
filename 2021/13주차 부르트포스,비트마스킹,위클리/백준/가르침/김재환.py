from itertools import combinations
N, K = map(int, input().split())
words = []
all = []
for _ in range(N):
    tmp = set(input()[4:-4])
    words.append(tmp)
    all += tmp
all = set(all)

if K < 5:
    print(0)
else:
    visited = 0
    for i in ['a', 'c', 'i', 't', 'n']:
        index = ord(i)-97
        visited = visited | (1 << index)  # 체크해줌
    K = K-5
    coms = list(combinations(all, K))
    get = 0
    for com in coms:
        tmpvisit = visited
        for ch in com:
            if (tmpvisit & (1 << ord(ch)-97)) == 0:  # 존재하지 않으면
                tmpvisit = tmpvisit | (1 << ord(ch)-97)
        # 이제 단어 비교
        total = 0
        for word in words:
            length = len(word)
            for ch in word:
                if tmpvisit & (1 << ord(ch)-97):  # 존재하면 길이 줄이기
                    length -= 1
            if length == 0:  # 전부 존재함
                total += 1
        get = max(get, total)
    print(get)
