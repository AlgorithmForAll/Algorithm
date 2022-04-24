"""
회문, 유사회문, 문자열 판별하기
"""


def calc(string):
    L = 0
    R = len(string)-1

    count = 0
    flag = 0
    while L <= R:
        if string[L] == string[R]:
            count += 1
            L += 1
            R -= 1
        elif string[L] == string[R-1] and string[L+1] == string[R]:
            if calc(string[L:R]) == 0:
                return 1
            elif calc(string[L+1:R+1]) == 0:
                return 1
            else:
                return 2
        elif string[L] == string[R-1] and flag == 0:
            if calc(string[L:R]) == 0:
                return 1
            else:
                return 2
        elif string[L+1] == string[R] and flag == 0:
            if calc(string[L+1:R+1]) == 0:
                return 1
            else:
                return 2
        else:
            return 2
    if len(string)//2 <= count and flag == 0:
        return 0
    elif len(string)//2 <= count and flag == 1:
        return 1
    else:
        return 2


N = int(input())
for n in range(N):
    tmp = input()
    print(calc(tmp))
