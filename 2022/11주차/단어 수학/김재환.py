"""
순열로 도전했으나 장렬히 사망
숫자 자체를 곱한다고 생각하고 풀기
ABB = A*100 + B*10 + B*1
"""
N = int(input())

words = []
dict = {}
for i in range(N):
    word = list(input())
    N = len(word)-1
    for w in word:
        if w not in dict:
            dict[w] = 10**N
        else:
            dict[w] += 10**N
        N -= 1
    words.append(word)
tmp = []
for k in dict:
    tmp.append([dict[k], k])
tmp.sort(key=lambda x: (-x[0]))
N = 9
newDict = {}
for t in tmp:
    score, alpha = t
    newDict[alpha] = N
    N -= 1
total = 0
for word in words:
    s = ""
    for w in word:
        s += str(newDict[w])
    total += int(s)
print(total)

"""
from itertools import permutations
N = int(input())

words = []
tmp = set()
for i in range(N):
    word = list(input())
    for w in word:
        tmp.add(w)
    words.append(word)

tmp = list(tmp)
tmp.sort()
dic = {}
for i in range(len(tmp)):
    dic[tmp[i]] = i
nums = [9-i for i in range(0, len(tmp))]
combs = list(permutations(nums))

answer = 0
for comb in combs:
    total = 0
    for word in words:
        nword = ""
        for w in word:
            nword += str(comb[dic[w]])
        total += int(nword)
    answer = max(answer, total)

print(answer)
"""
