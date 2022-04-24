"""
문자열 비교이기 때문에 kmp 개삘이다.

"""


def makePattern(n):
    st = "I"
    for i in range(n):
        st += "OI"
    return st


def kmpTable(st):

    tb = [0 for i in range(len(st))]
    j = 0
    for i in range(1, len(st)):
        while 0 < j and st[j] != st[i]:
            j = tb[j-1]

        if st[j] == st[i]:
            j += 1
            tb[i] = j
    return tb


def kmpCheck(st, tg, tb):
    count = 0
    #print(st, tg, tb)
    j = 0
    for i in range(len(tg)):
        while 0 < j and st[j] != tg[i]:  # 다른 경우 해당 인덱스를 옮겨 준다.
            j = tb[j-1]

        if st[j] == tg[i]:
            if j == len(st)-1:
                count += 1
                j = tb[j]
            else:
                j += 1

    print(count)


N = int(input())
M = int(input())
tg = input()
st = makePattern(N)
tb = kmpTable(st)
kmpCheck(st, tg, tb)
