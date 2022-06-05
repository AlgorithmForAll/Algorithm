"""
리스트를 만들어서 K만큼 순서대로 뽑고 해당되는 값을 Z로 만들어서 연산하기
"""

strmap = {}
nummap = {}
for i in range(10):
    strmap[str(i)] = i
    nummap[i] = str(i)
for i in range(ord('A'), ord('Z')+1):
    strmap[chr(i)] = i - ord('A') + 10
    nummap[i - ord('A') + 10] = chr(i)


def numToStr(num):
    tmp = []
    if num == 0:
        return ['0']
    while num != 0:
        tmp.append(nummap[num % 36])
        num = num // 36
    return tmp[::-1]


def strToNum(str):
    total = 0
    for i in range(len(str)):
        total += 36 ** i * strmap[str[len(str)-i-1]]
    return total


N = int(input())

# T = [[] for i in range(51)]
T = {}
W = []
for n in range(N):
    tmp = input()
    W.append(tmp)
    for i in range(len(tmp)):
        if tmp[len(tmp) - i - 1] not in T:
            T[tmp[len(tmp) - i - 1]] = 0
        T[tmp[len(tmp) - i - 1]] += (36**i * strmap['Z']) - \
            (36**i * strmap[tmp[len(tmp) - i - 1]])
K = int(input())

# T를 확인하며 K개 만큼 뽑는다.
sortDic = sorted(T.items(), key=lambda item: -item[1])
KL = set()
for i in sortDic:
    if K == 0:
        break
    else:
        KL.add(i[0])
        K -= 1
sum = 0
for word in W:
    w = list(word)
    for i in range(len(word)):
        if w[i] in KL:
            w[i] = 'Z'
    sum += strToNum(w)
print("".join(numToStr(sum)))
