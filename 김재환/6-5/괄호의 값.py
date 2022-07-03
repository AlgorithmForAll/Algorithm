"""
재귀를 이용해서 덩어리를 구해보고 덩어리 구해지면 세부숫자 곱하거나 더해서 구하기
"""

S = input()


def dung(total, S, start, end):

    s = []
    si = start

    if start == end:
        return 1

    for i in range(start, end):
        if S[i] == "]":
            if len(s) != 0 and s[-1] == '[':
                s.pop()
            else:
                return -1
        elif S[i] == ')':
            if len(s) != 0 and s[-1] == '(':
                s.pop()
            else:
                return -1
        else:
            s.append(S[i])
        if len(s) == 0:
            tmp = calc(S, si, i+1)
            total += tmp
            si = i+1
    return total


def calc(S, si, i):
    if S[si] == '(':
        return 2 * dung(0, S, si+1, i-1)
    if S[si] == '[':
        return 3 * dung(0, S, si+1, i-1)


tmp = dung(0, S, 0, len(S))
if tmp == -1:
    print(0)
else:
    print(tmp)
