
"""
그냥 in써도 되는데 kmp로 푸는 문제네
KMP풀자
"""
a = input()
b = input()

if b in a:
    print(1)
else:
    print(0)


def makeTable(word):
    tmp = [0 for i in range(len(word))]
    j = 0  # 비교대상 문자열
    i = 1
    while i < len(word):
        if word[j] == word[i]:  # 같으면 둘다 증가
            j += 1
            tmp[i] = j
            i += 1
        else:  # 일치하지 않음
            if j != 0:
                j -= 1
            else:
                tmp[i] = 0
                i += 1
    return tmp


tmp = makeTable("aaaak")
print(tmp)
